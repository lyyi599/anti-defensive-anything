---
name: anti-defensive-writing
description: Remove defensive language from writing. Use for writing and polishing papers (abstract, introduction, experiments, conclusion), rebuttals / reviewer responses, technical reports, resumes, cover letters, grant/project proposals, business plans, and formal emails. Triggers: polish paper, tighten prose, rebuttal, cover letter, write abstract, edit resume, too weak, too modest, 改论文、润色、写摘要、写 rebuttal、改简历、写申请书、语气太弱、太谦虚。
---

# Anti-Defensive Writing

Prerequisite: follow the core principles and honesty floor of `anti-defensive` (sibling directory `../anti-defensive/SKILL.md`).

> **A paper is a product launch, not a progress report.** Organize the whole piece around your single strongest advantage.

## Defensive signals

- Self-undermining: "unfortunately", "we must admit", "limited effect", "still clearly behind", "preliminary exploration"
- Report-style structure: "we first tried A, then B, and finally chose C"
- Results warehouse: every experiment piled in, none carrying a clear argumentative job
- Sudden self-negation at the end: the last sentence of the conclusion is full of limitations
- Pre-emptive defense: apologizing in the main text for problems reviewers haven't raised

## Rules

**Narrative**
1. The whole piece serves one core claim. Move anything unrelated to the appendix or delete it.
2. Don't set up contests you can't win: don't volunteer yourself into unfavorable comparisons.
3. State advantages explicitly, with numbers: "improves by 12.3%", not "some improvement".
4. Restructuring the story is allowed: if the strongest result isn't on the original storyline, change the storyline.

**Language**
5. Don't call a non-winning result a "loss"; state the fact: "on par with B", "B is higher under setting X".
6. Don't escalate a local phenomenon into a verdict on the whole method.
7. Delete buffer phrases that don't change the meaning: "we believe", "to some extent", "it is worth noting".

**Experiments**
8. Every experiment answers one question: which part of the claim does it prove? If you can't say, move it out.

**Structure**
9. Abstract/introduction = the launch opening: why the problem matters → what existing methods lack → what we did → evidence.
10. The conclusion only reinforces what should be remembered: what was solved, what was shown, why it matters. Limitations go in their own subsection, as factual sentences.

## Scene notes

- **Rebuttal**:
  - The first sentence is the response itself: what was done and what the result is. **Don't open with "We thank / We appreciate / We apologize"**; thanks are at most half a sentence, mid-sentence, or omitted.
  - New evidence supports only the range it actually covers: a gain on another in-domain dataset only lets you say "it also holds on a third in-domain dataset", not "it holds on unseen data / new domains". If the range the reviewer asked about isn't covered, say plainly that it isn't.
  - Agree with a reviewer's valid point in one sentence, then say what changed and where (section/table number).
- **Resume / cover letter**: verb + result + number. Delete contribution-diluting words like "participated in" or "assisted" if you actually led the work.
- **Proposals / business plans**: write the risk section as "risk → mitigation", not as a list of self-negations.
- **Email**: the first sentence says what you want; delete "sorry to bother you" and "if it's convenient, I wonder whether".

## Before / after

| Defensive | Anti-defensive |
|---|---|
| Although our method improves accuracy on two datasets, we must admit that we have not tested cross-domain generalization, so the results should be viewed with caution. | Our method improves accuracy on two in-domain datasets; cross-domain generalization has not been evaluated. |
| Our method is still clearly behind B in speed. | Our method trades 1.8× inference time for a 6.1-point accuracy gain. |
| We apologize for the confusion and thank the reviewer for pointing this out. We acknowledge that... | We clarified this in Sec. 3.2 (new Eq. 4). |
| We thank the reviewer for this valuable suggestion. Results on ADE20K (+2.4 mIoU) demonstrate that our method generalizes to new domains. | On ADE20K our method gains +2.4 mIoU, so the improvement holds on a second scene-parsing benchmark. Transfer to other domains (e.g., medical images) is untested; we note this in Sec. 6. |
| Participated in optimizing the recommendation system, with some positive results. | Rewrote the retrieval module; online CTR +4.2%. |

## Must keep

- Real limitations that affect how credible the conclusion is (as factual sentences in the limitations subsection).
- Fair comparison with strong baselines — "don't set up contests" means don't volunteer a losing narrative, not hide standard baselines.
- On a resume, never present participation as leadership.
