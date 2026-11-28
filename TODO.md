# TODO

Current focus: the three core components — `anti-defensive` (core rules + router), `anti-defensive-writing`, and `anti-defensive-ideation`.

## Parked skills

These were removed from the plugin because evals could not show an effect over the no-plugin baseline. The last versions (skill + eval cases) are in commit `ddf2af7`:

```bash
git checkout ddf2af7 -- skills/anti-defensive-<scene> evals/<case>
```

| Skill | Eval cases at `ddf2af7` | Why parked | What would bring it back |
|---|---|---|---|
| `anti-defensive-coding` | `coding-cleanup`, `coding-write-internal`, `coding-add-feature` | The baseline already scored full marks on all three; the current model isn't defensive on small, clear coding tasks. The skill also rarely triggered on plain "write a function" requests. | A case where the baseline is defensive: multi-file edits in a real repo, code around external services, or a long agentic session. |
| `anti-defensive-advice` | `advice-db-choice` | With a fair rubric, the baseline also scored 3/3. The earlier gap came from a rubric that demanded the flip condition "in one sentence". | Questions where the model typically hedges: underspecified trade-offs, judgment calls with real uncertainty, pushback from the user without new arguments. |
| `anti-defensive-agent` | `agent-report` | Split graders showed 0.93 vs 0.87. Both arms disclosed failures honestly; the earlier gap came from a combined rubric. | A multi-step agent task (not a report written from a given summary) where over-asking or escape-hatch reports actually happen. |

## Core components

- [x] Ideation: read the baseline's failing outputs. The gap is real: the baseline's ideas (RL agents that look for evidence, streaming memory, diagnostic benchmarks, synthetic data) are exactly the field's current consensus, while the plugin arm adds ideas the baseline never produced (codec-domain tokens, event-segmentation memory, writing the video into weights). Caveat: the baseline's "diagnostic benchmark" idea matches an idea the plugin arm labeled "contrarian", and only the labeled one passed, so the judge may be swayed by tier labels.
- [x] Ideation: the bold-idea grader now ignores self-applied labels and treats directions the field already pursues as incremental. Result unchanged: 3/3 vs 0/3.
- [x] Writing: added `writing-conclusion` (ASR conclusion paragraph). It exposed a real gap: the skill let conclusions end on future work (1/3). Added rule 8 "End on the takeaway"; now 3/3 vs 0/3.
- [x] Writing: replaced the LLM "honest scope" grader with two regexes (`keeps-limitation`, `no-overclaim`), tested on every past output. Rebuttal: keeps-limitation 3/3 vs 1/3, no-overclaim 3/3 vs 2/3; the baseline failures were read and are real (dropped the "untested" fact, or claimed transfer to new domains).
- [x] Writing: tried subtler hedging in a held-out English abstract (`evals-holdout/writing-abstract-en`). The baseline also removes "we believe", "to some extent", "attempt to" and opens with the contribution (3/3 in both arms). Conclusion: the current model already strips hedging phrases; the writing skill's real effects are structural (what comes first, what comes last, how far a claim reaches). Phrase-level graders stay as guards.
- [ ] Writing: the held-out abstract baseline ended on a limitation in 1 of 3 runs. If that recurs, add an `ends-on-takeaway` grader to a scene case (not to the held-out one).
