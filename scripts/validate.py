#!/usr/bin/env python3
"""Repository consistency checks (standard library only). Run locally and in CI.

Checks:
  1. every skill: SKILL.md exists, frontmatter has name/description, name matches the directory
  2. scene skills point to the core principles ../anti-defensive/SKILL.md
  3. the routing table and the scene skill directories match one-to-one
  4. plugin.json and marketplace.json versions match, and CHANGELOG has that version
  5. stale translations (warning only, never fails): see scripts/translate.py
  6. every scene has at least one eval case (evals/<scene>-*/)
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILLS = REPO / "skills"
COMMON = "anti-defensive"
errors = []


def frontmatter(path: Path) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
    if not m:
        return {}
    return {k.strip(): v.strip() for k, v in (l.split(":", 1) for l in m.group(1).splitlines() if ":" in l)}


# 1-2. skills
skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
for d in skill_dirs:
    f = d / "SKILL.md"
    if not f.exists():
        errors.append(f"{d.name}: missing SKILL.md")
        continue
    fm = frontmatter(f)
    if fm.get("name") != d.name:
        errors.append(f"{d.name}: frontmatter name={fm.get('name')!r} does not match the directory")
    if not fm.get("description"):
        errors.append(f"{d.name}: missing description")
    if d.name != COMMON and f"../{COMMON}/SKILL.md" not in f.read_text(encoding="utf-8"):
        errors.append(f"{d.name}: does not point to the core principles ../{COMMON}/SKILL.md")

# 3. router
domains = {d.name for d in skill_dirs if d.name != COMMON}
router = (SKILLS / COMMON / "SKILL.md").read_text(encoding="utf-8")
routed = set(re.findall(r"\|\s*`(anti-defensive-[\w-]+)`\s*\|", router))
errors += [f"routing table is missing scene: {n}" for n in sorted(domains - routed)]
errors += [f"routing table points to a missing scene: {n}" for n in sorted(routed - domains)]

# 4. version
plugin = json.loads((REPO / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
market = json.loads((REPO / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
version = plugin.get("version")
for entry in market.get("plugins", []):
    if entry.get("name") == plugin.get("name") and entry.get("version") != version:
        errors.append(f"version mismatch: plugin.json={version} marketplace.json={entry.get('version')}")
changelog = REPO / "CHANGELOG.md"
if not changelog.exists() or not re.search(rf"^## \[?{re.escape(str(version))}\]?", changelog.read_text(encoding="utf-8"), re.M):
    errors.append(f"CHANGELOG.md has no entry for the current version {version}")


# 5. translations: stale translations are a warning, not an error
sys.path.insert(0, str(REPO / "scripts"))
from translate import PAIRS, REASON, status  # noqa: E402

warnings = []
for src, dst, _ in PAIRS:
    state, _, _ = status(src, dst)
    if state != "ok":
        warnings.append(f"translation {dst} needs regenerating: {REASON[state]} (source {src}). Run python3 scripts/translate.py")

# 6. evals
evals = REPO / "evals"
for name in sorted(domains):
    short = name[len(COMMON) + 1:]
    if not any(evals.glob(f"{short}-*/prompt.md")):
        errors.append(f"scene {short} has no eval case (evals/{short}-*/prompt.md)")

for w in warnings:
    print(f"⚠ {w}")
if errors:
    print("\n".join(f"✗ {e}" for e in errors))
    sys.exit(1)
print(f"✓ {len(skill_dirs)} skills, {len(routed)} routed scenes, version {version}, every scene has evals")
