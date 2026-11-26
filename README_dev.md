# Developer guide

For people changing rules, adding scenes, or cutting releases. To just use the skills, see [README.md](README.md). Open work is in [TODO.md](TODO.md).

The working language is **English**. Chinese docs are generated (see [Languages](#languages)).

## Layout

```
skills/
├── anti-defensive/            # core rules + router + honesty floor
├── anti-defensive-writing/    # papers, rebuttals, reports, resumes, emails
└── anti-defensive-ideation/   # brainstorming, research ideas
evals/                         # eval cases (claude plugin eval)
prompts/quick-prompt.md        # paste-in prompt for tools without skills
scripts/                       # install.sh, validate.py, translate.py
assets/                        # logo; src/gen_logo.py generates it
.claude-plugin/                # plugin + marketplace manifests
README_CN.md, prompts/quick-prompt-zh.md   # generated Chinese versions
```

## How it works

Each skill has its own `description`, so the agent can trigger any of them directly. The core skill routes to a scene skill, and each scene skill starts by pointing back to the core rules. Either way in, the core rules and the honesty floor apply.

## Skill format

Keep skills short and scannable (aim for under ~80 lines). Every scene skill uses the same sections:

1. **One-line principle**, as a quote
2. **Why**: one short paragraph on the model's default behavior that the skill corrects
3. **Rules**: numbered, imperative, one line each
4. **Quick checks**: concrete things to search for before returning
5. **Before / after**: 2–3 rows, from domains unrelated to the eval cases
6. **Must keep**: which "defenses" are correct
7. **Return** (optional): what the output should contain

The skill's `description` carries English and Chinese trigger words, so Chinese requests trigger it too.

## Local development

```bash
scripts/install.sh --link                             # symlink into ~/.claude/skills
scripts/install.sh --link writing                     # only some scenes (core is always included)
scripts/install.sh --link --target ./.claude/skills   # project-level
```

## Checks

```bash
python3 scripts/validate.py     # structure, routing table, versions, CHANGELOG, eval coverage; warns on stale translations
claude plugin validate .        # plugin + marketplace manifests
```

CI runs `validate.py` and an install smoke test on every push and PR.

## Evals

`validate.py` only checks shape. Evals check whether a rule changes behavior.

```
evals/writing-rebuttal/
├── prompt.md          # a request that tends to trigger defensiveness
└── graders/           # one question per grader: regex or LLM rubric, plus a skill-fired indicator
```

```bash
claude plugin eval . --case 'writing-*' --judge-model sonnet   # 3 runs per case plus a no-plugin baseline
```

- Case prompts are in **Chinese** on purpose, to check that the English skills work for Chinese-speaking users. Rubrics are English.
- Needs git ≥ 2.31 (a user-space git via micromamba works). Results go to `evals/results/` (gitignored). Add `--no-publish` to keep reports local.
- Every case plants something that **must stay** (a real limitation, a number), so a skill can't be tuned into blind deletion or overclaiming.
- Skill examples must not reuse eval content; otherwise the eval tests copying, not the rule.
- Regex uses JavaScript syntax: `flags: i` instead of `(?i)`.

Lessons from auditing the rubrics. Each of these once produced a fake or inflated effect:

- **One question per grader.** A combined rubric hides which item failed and lets one strict item decide the result.
- **Read the baseline's failing outputs before trusting a gap.** If the baseline output is fine, the rubric is wrong.
- **Spell out what does not count as a violation**, especially borderline phrasing.
- **Test the intent, not a hard count** (e.g. not "in one sentence").
- **Split results by whether the skill fired.** A skill that didn't trigger behaves like the baseline; that's a trigger problem, not a rule problem.
- **Judge with sonnet.** The default haiku splits votes on long outputs.

Issues filed with the "defensive case" template can be turned directly into a `prompt.md` and graders.

## Languages

- **Skills are English only.** Replies follow the user's language. A side-by-side eval of Chinese and English skills showed no advantage either way.
- **English docs are the source; Chinese docs are generated.** `README_CN.md` and `prompts/quick-prompt-zh.md` start with a line recording the source file's hash. Don't edit them by hand.

```bash
python3 scripts/translate.py --check   # list stale translations (no model call)
python3 scripts/translate.py           # regenerate stale ones (needs the claude CLI)
```

A stale translation is a warning, never a CI failure. To translate another file or add a language, add a row to `PAIRS` in `scripts/translate.py`.

## Logo

Change `PARAMS` in `assets/src/gen_logo.py`, then run it (PNGs need Pillow).

## Releasing

1. In `CHANGELOG.md`, turn `[Unreleased]` into the version and date, and describe each scene's behavior change.
2. Bump `version` in both `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.
3. After the checks and evals pass, commit and push to `main`.
