# Changelog

The version lives in both `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`; `scripts/validate.py` checks they match and that this file has an entry for it.

Rule changes change model behavior, so every entry says **which scene and what behavior changed**.

## [Unreleased]

### Changed
- **README redesign**: centered header with logo, badges (CI, version, license), quick nav, a before/after table, and the eval results; install options for other tools folded into `<details>`. The translator now rewrites in-page anchors to the translated headings.
- **Focus on three core components**: `anti-defensive` (core), `anti-defensive-writing`, `anti-defensive-ideation`. All three were rewritten to a short, scannable format modeled on lean community skills: principle → why → numbered rules → quick checks → before/after → must keep (core 34 lines, writing 58, ideation 68). Ideation gained a calibration list of the idea clusters models default to; writing gained a quick-check list of concrete phrases to remove and a "return" contract.

- `writing`: new rule 8, "End on the takeaway": the last sentence of a conclusion, abstract, or reply says what the result means; limitations and future work go before it. The new `writing-conclusion` case showed the skill still let conclusions end on future work (1/3); after the rule, 3/3 (baseline 0/3).
- Evals: `writing-rebuttal`'s LLM "honest scope" grader was replaced by two regexes (`keeps-limitation`, `no-overclaim`) tested on all past outputs; the ideation `bold-idea` grader now ignores self-applied labels such as "contrarian" or "moonshot". Current results, 3 runs each vs no-plugin baseline: rebuttal opens with the response 3/3 vs 0/3, keeps the untested limitation 3/3 vs 1/3, no overclaim 3/3 vs 2/3; conclusion ends on the takeaway 3/3 vs 0/3; ideation has a non-incremental idea 3/3 vs 0/3.

### Added
- `writing-conclusion` eval case.

### Removed
- `anti-defensive-coding`, `anti-defensive-advice`, `anti-defensive-agent` and their eval cases are parked (see `TODO.md`; restorable from commit `ddf2af7`): evals could not show an effect over the no-plugin baseline.
- `templates/` and the "new scene" issue template.

- **Working language is now English.** Skills, `README.md`, developer docs, scripts, and grader rubrics are written in English. Chinese is an additional entry point: `README_CN.md` and `prompts/quick-prompt-zh.md` are generated from the English sources by `scripts/translate.py`. Eval case prompts stay in Chinese to check that the English skills work for Chinese-speaking users. Skill trigger words remain bilingual.
- All skills switched to English. Same rules, examples, and boundaries as the Chinese versions. A side-by-side eval on the same cases: Chinese skills triggered 18/23 with 55/55 grader passes; English skills 14/21 with 50/51 — no meaningful difference.

- `writing`: the before/after example that resembled the `writing-rebuttal` eval (two in-domain datasets, cross-domain untested) was replaced with an unrelated one (compiler pass on ARM boards vs. GPUs), and the rebuttal rule no longer echoes the eval's wording. Triggers also cover "rewrite / revise / reviewer response / 改写 / 回复审稿意见".
- Evals: `writing-rebuttal` and `agent-report` rubrics split into single-question graders, judged with sonnet. A "no invention" grader for writing was removed after it failed both arms on outputs that invented nothing.

### Added
- `scripts/translate.py`: generates translations from a source file and records the source hash on the first line; `validate.py` warns on stale translations without failing CI.

### Known issues
- `writing` (re-audit of 0.2.0): with single-question graders, the robust effect is **opening with the response instead of thanks** — passed every run where the skill fired, 0/9 without the plugin. "Honest scope" (keep the untested-cross-domain caveat, don't overclaim) showed only a small, noisy difference (2/3 vs 1/3 in the last round); the judge splits on borderline phrasing. The skill fired in 12 of 14 runs across rounds; when it didn't fire, output matched the baseline.
- `agent` (correction to 0.2.0): split graders show almost no difference (0.93 vs 0.87). Both arms disclose the failing test and the missing staging check; both sometimes open with a heading and the root cause instead of "fixed". The 0.2.0 gap (1.00 vs 0.67) came from the combined rubric.
- `advice` (correction to 0.2.0): the `advice-db-choice` rubric required stating the flip condition "in one sentence". Relaxed to its intent — briefly state when the recommendation would change, instead of comparing every case — the no-plugin baseline also scores 3/3. The 0.2.0 gap (1.00 vs 0.50) came mainly from that strict rubric item, not from the plugin making the model lead with a recommendation. Like `coding`, this case currently can't show the skill's effect; it stays as a regression guard.

### Removed
- `validate.py`'s hard check that the Chinese and English README tables have the same number of rows (replaced by the stale-translation warning).

## [0.2.0] - 2026-11-26

### Changed
- `agent`: triggers now cover "write the final report / status update / fix write-up". Such requests previously didn't trigger the skill; now `agent-report` triggers 3/3 and scores 1.00 (no-plugin baseline 0.67).
- `advice`: triggers now cover choice questions like "A or B / which one / should I". Previously not triggered; now `advice-db-choice` triggers 3/3 and scores 1.00 (baseline 0.50).
- `writing`: rebuttal rules now say "the first sentence is the response itself; don't open with thank/apologize", and new evidence may only claim the range it covers (a new in-domain dataset ≠ a new domain). Before: 1 of 2 runs opened with thanks and overstated generalization; after: `writing-rebuttal` 5/5 pass (baseline 0/5).
- `coding`: triggers now cover ordinary coding requests ("write a function / implement / add a feature / fix a bug").
- Evals: the `ideation-research` rubric was split into 4 single-question graders (bold idea / first choice / no hedging in the list / no fabrication) and judged by sonnet; votes are now unanimous: with plugin 1.00, without 0.60 (the baseline produced no non-incremental idea in 3/3 runs). Added the `coding-add-feature` case.

### Known issues
- `coding`: all three cases (cleanup, writing an internal function, adding a feature to existing code) score full marks without the plugin — the current model isn't defensive on such small tasks, so the skill's effect can't be measured. Even with the wider triggers, the skill rarely fires (1 of 6 runs across two cases). The cases stay as regression guards.

## [0.1.0] - 2026-11-26

### Added
- Core principles + router skill `anti-defensive`, including the honesty floor.
- Scene skills: `writing`, `coding`, `ideation`, `advice`, `agent`.
- Chinese and English quick prompts, a new-scene template, install and validation scripts.
- Claude Code plugin and marketplace manifests.
- Logo (a star breaking through a shield) and its generator `assets/src/gen_logo.py`.
- Per-scene eval cases (`evals/`), run with `claude plugin eval`.
- CI: runs `scripts/validate.py` on push and PR.
