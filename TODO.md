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
- [ ] Ideation: make the bold-idea grader ignore self-applied labels ("contrarian", "moonshot") and judge the idea itself.
- [ ] Writing: add a second eval case outside rebuttals (abstract or conclusion), where self-undermining language is common.
- [ ] Writing: the "honest scope" grader still splits on borderline phrasing; tighten it or replace it with a regex for the untested-limitation sentence.
