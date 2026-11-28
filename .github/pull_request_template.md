## What changes

<!-- One or two sentences. For a rule change: which behavior should change, and on which kind of request. -->

## Checklist

- [ ] `python3 scripts/validate.py` passes
- [ ] Changed `skills/`? Ran `claude plugin eval . --case '<scene>-*' --judge-model sonnet --json <file>` and `python3 scripts/eval_compare.py <file>`, with no regressions (or explained below)
- [ ] Changed a skill `description`? Also ran the `negative-*` cases
- [ ] No eval content (dataset names, numbers, sentences) copied into a skill
- [ ] The honesty floor is not weakened: real limitations, unknowns, and unverified items still stay
- [ ] `CHANGELOG.md` `[Unreleased]` describes the behavior change
- [ ] Edited `README.md` or `prompts/quick-prompt.md`? Ran `python3 scripts/translate.py`

## Eval results

<!-- Paste the eval_compare.py output, or say why evals were not needed (docs-only change). -->
