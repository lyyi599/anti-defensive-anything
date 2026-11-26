---
name: anti-defensive-writing
description: Removes defensive writing (hedges, pre-emptive apologies, self-undermining limitations, process narration) while keeping every fact and every real limitation. Use whenever the user asks to write, rewrite, revise, or polish papers (abstract, introduction, experiments, conclusion), rebuttals and reviewer responses, reports, proposals, resumes, cover letters, or emails. Triggers: rewrite, revise, polish, tighten, rebuttal, respond to reviewers, abstract, cover letter, resume, 改写、修改、润色、改论文、写摘要、写 rebuttal、回复审稿意见、改简历、写申请书、语气太弱、太谦虚.
---

# Anti-Defensive Writing

Apply the rules and honesty floor in `../anti-defensive/SKILL.md` first.

> A paper is a launch, not a progress report. Build it around the strongest result.

Defensive writing apologizes before anyone objects, narrates what was tried instead of what was found, and closes on a self-verdict. Reviewers read that as a lack of confidence and start looking for the weakness you just pointed at.

## Rules

1. **Open with the point.** The first sentence of a section, paragraph, or reply is the claim or what was done. Not thanks, background, or process.
2. **One storyline.** Everything serves the core claim. Move the rest to the appendix or cut it.
3. **Numbers, not adjectives.** "+12.3%", not "a notable improvement".
4. **No contests you can't win.** Don't build the story on a metric you lose. State the trade-off once: "1.8× slower for +6.1 accuracy".
5. **Limits as facts, in their place.** One factual sentence, before the closing. Not an apology in the introduction.
6. **Claim only what the evidence covers.** More results in the same setting support that setting. They are not evidence of generalization to new domains.
7. **Every experiment has a job.** If you can't say which part of the claim it proves, move it out.
8. **End on the takeaway.** The last sentence of a conclusion, abstract, or reply says what the result means or enables. Limitations and future work go before it, never last.

## Quick checks

Before returning the text, find and fix:

- Openers: "We thank…", "We apologize…", "It is worth noting that…", "In this section, we…"
- Self-undermining words: unfortunately, merely, only, limited, preliminary, still lags, we must admit
- Stacked hedges: may potentially, to some extent, somewhat, arguably
- Process narration: "we first tried…, then…, finally…"
- A last sentence that is a limitation, a caveat, or future work
- A claim of improvement with no number

## By genre

- **Rebuttal**: the response comes first ("We added X: +Y over Z"). Agree with a valid point in one sentence, then say what changed and where (Sec./Table).
- **Resume**: verb + result + number. Write "led" only if you led it.
- **Email**: the first sentence says what you need.
- **Proposal**: write risks as "risk → mitigation", not as a list of doubts.

## Before / after

| Defensive | Anti-defensive |
|---|---|
| Although our compiler pass cuts latency on two ARM boards, we must admit we have not measured it on GPUs, so the results should be viewed with caution. | Our compiler pass cuts latency on two ARM boards; GPU performance has not been measured. |
| We thank the reviewer for this valuable suggestion. Results on ADE20K (+2.4 mIoU) demonstrate that our method generalizes to new domains. | On ADE20K our method gains +2.4 mIoU, so the improvement holds on a second scene-parsing benchmark. Transfer to other domains is untested; Sec. 6 now says so. |
| Participated in optimizing the recommendation system, with some positive results. | Rewrote the retrieval module; online CTR +4.2%. |

## Must keep

- Every fact, number, and citation in the source.
- Limitations that affect how far the conclusion can be trusted.
- Fair comparison with standard baselines. "No contests you can't win" means don't volunteer a losing narrative, not hide a baseline.

## Return

The revised text. If you removed or changed a claim (not just its wording), list it in at most three bullets after the text, unless the user asked for the text only.
