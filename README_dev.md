# Developer guide

For people changing rules, adding scenarios, or cutting releases. To just use the skills, see [README.md](README.md).

The working language of this repository is **English**: skills, docs, scripts, and grader rubrics are written in English. Chinese docs are generated (see [Languages](#languages)).

## Layout

```
skills/
├── anti-defensive/            # core principles + router (common + router)
├── anti-defensive-writing/    # papers, rebuttals, resumes, proposals, emails
├── anti-defensive-coding/     # swallowed errors, silent fallbacks, over-abstraction
├── anti-defensive-ideation/   # brainstorming, research ideas
├── anti-defensive-advice/     # technology choices, decisions, reviews, feedback
└── anti-defensive-agent/      # agent execution: over-asking, escape-hatch reports
prompts/quick-prompt.md        # paste-in prompt for tools without skills (quick-prompt-zh.md is generated)
templates/SKILL.template.md    # template for a new scenario
scripts/install.sh             # install
scripts/validate.py            # consistency checks
scripts/translate.py           # generates Chinese docs from English sources
evals/                         # per-scenario eval cases (claude plugin eval)
.claude-plugin/                # Claude Code plugin + marketplace manifests
.github/                       # CI and issue templates
assets/                        # logo.svg, logo.png, icon.png; src/gen_logo.py generates them
README_CN.md                   # Chinese entry point (generated)
CHANGELOG.md                   # behavior changes per version
CLAUDE.md                      # maintenance conventions for Claude
```

## How it works

```
user request ──► anti-defensive (core principles + routing table) ──► loads the matching scene skill
                                                      │
scene keywords match directly ──► anti-defensive-xxx ─┘ the scene skill reads the core principles first
```

- **Both entry points work**: every skill has its own `description`, so the agent triggers it by keyword; every scene skill starts by pointing to `../anti-defensive/SKILL.md`, so the core principles apply however you enter.
- **The routing table** lives in `skills/anti-defensive/SKILL.md`, one row per scene: signals → which skill to load.
- **The honesty floor** is in the core principles and shared by every scene: anti-defensive ≠ overclaiming. Decision-changing risks, unverified items, and unknowns must stay.

## Local development

Install as symlinks so edits take effect immediately:

```bash
scripts/install.sh --link                             # link into ~/.claude/skills
scripts/install.sh --link coding ideation             # only some scenes (the core skill is always included)
scripts/install.sh --link --target ./.claude/skills   # project-level
```

## Adding a scenario

1. Copy `templates/SKILL.template.md` to `skills/anti-defensive-<domain>/SKILL.md` and fill it in.
2. Add a row to the routing table in `skills/anti-defensive/SKILL.md`.
3. Add at least one `<domain>-*` case under `evals/` (see [Evals](#evals)).
4. If useful, add a rule to `prompts/quick-prompt.md` and an example row to the usage table in `README.md`, then run `python3 scripts/translate.py` to regenerate the Chinese versions.
5. Run the checks and the scene's evals.

Every scene skill has the same five sections: **one-line principle → defensive signals → rules → before/after → must keep**. The last one matters most: it says which defenses are correct.

## Checks

```bash
python3 scripts/validate.py     # structure, routing table, versions, CHANGELOG, eval coverage; warns on stale translations
claude plugin validate .        # plugin + marketplace manifests
```

CI (`.github/workflows/validate.yml`) runs `validate.py` and an install smoke test on every push and PR.

## Evals

`validate.py` only checks shape; whether a rule works is what evals are for. Cases live in `evals/<scene>-<name>/`:

```
evals/advice-db-choice/
├── prompt.md                    # a request that tends to trigger defensiveness (frontmatter: tags, runs, allowed_tools)
└── graders/
    ├── no-defensive-phrases.md  # regex: typical defensive phrases must not appear
    ├── criteria.md              # LLM rubric: anti-defensive traits + honesty floor (what must stay)
    └── skill-fired.md           # indicator: did the skill trigger (not scored against the baseline)
```

Run:

```bash
claude plugin eval . --case 'advice-*'      # run the scene you changed; default 3 runs per case plus a no-plugin baseline
claude plugin eval .                        # everything
```

- Case prompts are deliberately written in **Chinese**: they check that the English skills trigger and work for Chinese-speaking users. Rubrics are in English.
- Requires git ≥ 2.31. If the system git is older, install a user-space git (e.g. with micromamba) and put it first on PATH.
- Skill examples must not reuse eval content (datasets, numbers, sentences); otherwise the eval tests copying, not the rule.
- Every case plants something that **must stay** (a real limitation, a boundary check, a failing test), so a skill can't be tuned into blind deletion or overclaiming.
- Regex graders see the whole reply, including explanations; when matching code, include syntax (e.g. `except Exception\s*:` on indented lines with `flags: m`) to avoid false positives.
- Use `flags: i` for case-insensitive matching, not `(?i)` (the evaluator uses JavaScript regex).
- Results go to `evals/results/` (gitignored). Reports are published to claude.ai by default; pass `--no-publish` to keep them local.
- Single runs are noisy; judge a change on at least the default 3 runs.
- For open-ended output (e.g. ideation): one rubric per question, and spell out what does **not** count as a violation; use `--judge-model sonnet`, since the default haiku splits votes on long outputs.

Lessons from auditing the rubrics (each of these once produced a fake or inflated effect):

- **One question per grader.** A combined "all of 1–4" rubric hides which item failed and lets one strict item decide the result.
- **Read the baseline's failing outputs before trusting a gap.** If the baseline output is actually fine, the rubric is wrong, not the model.
- **Write out what does not count as a violation**, especially for borderline phrasing (e.g. "the gain holds beyond the original datasets" is an accurate in-domain claim, not overclaiming).
- **Don't encode style as a hard count** (e.g. "in one sentence"); test the intent.
- **Split results by whether the skill fired.** A skill that didn't trigger behaves like the baseline; that is a trigger problem, not a rule problem.

Issues filed with the "defensive case" template can be turned directly into `prompt.md` + `criteria.md`.

## Languages

- **Skills are English only.** Replies follow the user's language regardless of the skill's language. A side-by-side eval of Chinese vs. fully translated English skills showed no advantage either way. Only the trigger words in `description` are bilingual (English + Chinese).
- **Human docs: English is the source, Chinese is generated.** `README_CN.md` and `prompts/quick-prompt-zh.md` start with a line recording their source file and its hash. Don't edit them by hand.

```bash
python3 scripts/translate.py --check   # which translations are stale (no model call)
python3 scripts/translate.py           # regenerate stale translations (needs the claude CLI; sonnet by default)
python3 scripts/translate.py --force   # regenerate everything
```

- A stale translation is a warning, never a failure: `validate.py` and CI report it, but it doesn't block a change.
- To translate a new file or add a language, add a row to `PAIRS` in `scripts/translate.py` (source, target, language).
- Links between files (e.g. `README.md` → `README_CN.md`) are rewritten by the script; mechanical replacements live in code, not in the model's instructions.

## Logo

Change only `PARAMS` in `assets/src/gen_logo.py`, then run `python3 assets/src/gen_logo.py` to regenerate `logo.svg`, `logo.png`, and `icon.png` (PNGs need Pillow).

## Releasing

1. In `CHANGELOG.md`, turn `[Unreleased]` into the new version and date, and describe each scene's behavior change.
2. Bump `version` in both `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` (`validate.py` checks they match and that the CHANGELOG has the entry).
3. After the checks and relevant evals pass, commit and push to `main`; users get the new version by updating the plugin in Claude Code.
