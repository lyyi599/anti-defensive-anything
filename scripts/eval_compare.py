#!/usr/bin/env python3
"""Compare a `claude plugin eval --json` result with evals/baseline.json and flag regressions.

    claude plugin eval . --judge-model sonnet --no-publish --json out.json
    python3 scripts/eval_compare.py out.json            # print a table, exit 1 on a regression
    python3 scripts/eval_compare.py out.json --update   # write these scores into the baseline

The baseline stores, per case and grader, how many runs passed in each arm ("with" = plugin,
"without" = no-plugin baseline). Only the "with" arm is checked for regressions. With 3 runs,
one run of difference is noise, so a grader is flagged only when its pass rate drops by more
than 1/3 (e.g. 3/3 → 1/3). Cases not in the result file are left untouched by --update.
"""
import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BASELINE = REPO / "evals" / "baseline.json"
NOISE = 1 / 3 + 1e-9


def summarize(result: dict) -> dict:
    """{case: {"runs": n, "graders": {grader: {"with": passed, "without": passed|None}}}}"""
    out = {}
    for case in result["cases"]:
        arms = case["arms"]
        graders = {}
        for arm, runs in arms.items():
            for run in runs:
                for g in run["graders"]:
                    entry = graders.setdefault(g["name"], {"with": 0, "without": None})
                    if arm == "without":
                        entry["without"] = (entry["without"] or 0) + int(g["passed"])
                    else:
                        entry["with"] += int(g["passed"])
        out[case["name"]] = {"runs": len(arms.get("with", [])), "graders": graders}
    return out


def fmt(passed, runs):
    return "–" if passed is None else f"{passed}/{runs}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("result", help="JSON written by claude plugin eval --json")
    ap.add_argument("--update", action="store_true", help="accept these scores as the new baseline")
    args = ap.parse_args()

    result = json.loads(Path(args.result).read_text(encoding="utf-8"))
    new = summarize(result)
    base = json.loads(BASELINE.read_text(encoding="utf-8")) if BASELINE.exists() else {"cases": {}}

    regressions = []
    print(f"{'case':<22} {'grader':<26} {'with':>6} {'base':>6} {'without':>8}")
    for case, data in new.items():
        old = base["cases"].get(case)
        for grader, g in data["graders"].items():
            runs = data["runs"]
            prev = old and old["graders"].get(grader)
            mark = ""
            if prev:
                before = prev["with"] / old["runs"]
                now = g["with"] / runs if runs else 0
                if before - now > NOISE:
                    mark = "  ✗ regression"
                    regressions.append(f"{case}/{grader}: {fmt(prev['with'], old['runs'])} → {fmt(g['with'], runs)}")
            else:
                mark = "  (new)"
            base_s = fmt(prev["with"], old["runs"]) if prev else "–"
            print(f"{case:<22} {grader:<26} {fmt(g['with'], runs):>6} {base_s:>6} {fmt(g['without'], runs):>8}{mark}")

    print(f"\ncost ${result.get('costUsd', 0):.2f}, judge {result['suite'].get('judgeModel')}, claude {result.get('claudeVersion')}")
    if args.update:
        base.setdefault("cases", {}).update(new)
        base["updated"] = result.get("startedAt", "")[:10]
        base["claudeVersion"] = result.get("claudeVersion")
        base["judgeModel"] = result["suite"].get("judgeModel")
        BASELINE.write_text(json.dumps(base, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
        print(f"✓ baseline updated: {BASELINE.relative_to(REPO)}")
        return 0
    if regressions:
        print("✗ regressions (read the failing outputs before deciding):")
        print("\n".join(f"  {r}" for r in regressions))
        return 1
    print("✓ no regressions against the baseline")
    return 0


if __name__ == "__main__":
    sys.exit(main())
