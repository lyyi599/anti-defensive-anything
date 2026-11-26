---
name: anti-defensive-ideation
description: Remove defensiveness from ideation. Use for brainstorming, research topic selection, paper ideas, solution concepts, product ideas, creative divergence. Avoid offering only incremental improvements or consensus ideas, self-censoring while generating, and attaching "but this may be challenging" to every idea. Triggers: brainstorm, research ideas, novel ideas, think bigger, new directions, 想 idea、头脑风暴、选题、有什么新思路、研究方向。
---

# Anti-Defensive Ideation

Prerequisite: follow the core principles and honesty floor of `anti-defensive` (sibling directory `../anti-defensive/SKILL.md`).

> **Separate generating from judging. Don't censor while generating; don't go easy while judging.**

The roots of defensive ideation: the model tends to output the "most typical" answer (mode collapse), and it limits itself by feasibility while still generating, so all that's left are safe incremental improvements.

## Defensive signals

- The listed ideas are the ones anyone in the field would think of first
- All of them are "add module Y on top of X" or "apply method A to dataset B"
- Every idea is followed by "but may face data/compute/feasibility challenges"
- Several ideas are the same idea reworded
- Not a single idea makes you think "this is a bit crazy"

## Process

**1. Rule out the consensus first.**
List the 3–5 most obvious ideas for this problem, mark them as the "consensus zone", and don't propose them or their variants afterwards.

**2. Generate in tiers (no risks or feasibility at this stage).**
Each round covers at least four tiers:

| Tier | Meaning |
|---|---|
| Incremental | a clear improvement on the existing route |
| Cross-domain | a mechanism, tool, or perspective borrowed from another field |
| Contrarian | challenges one assumption the field takes for granted |
| Moonshot | if it worked, it would change how this field works |

The incremental tier is at most a quarter.

**3. Amplify first, then converge.**
For promising ideas, push them to their most radical version first, then pull back to a doable version. Don't start from the safe version.

**4. Judge (a separate stage).**
Score value and feasibility **separately**; "not sure it can be built" must not drag down the score of "it matters if built". Then give a clear ranking and a first choice.

## How to write each idea

```
Name: one sentence
Core insight: the non-obvious bet it makes
Why now: what changed to make it feasible
Minimal test: the smallest experiment you can run within a week
```

## Before / after

| Defensive | Anti-defensive |
|---|---|
| You could try adding an attention mechanism to the existing model to improve performance, but note that the compute cost may increase. | Contrarian: remove attention. Bet that the task's dependencies are local; replace it with convolutions + explicit long-range memory. Minimal test: compare on an LRA subset. |
| Here are several possible directions, each with pros and cons; choose based on your situation. | First choice #3: highest value, and the minimal test takes only two days. #1 is safe but has a low ceiling. |

## Must keep

- In the judging stage, state fatal risks truthfully (ethics, hard physical/mathematical constraints that make it fundamentally infeasible).
- Don't fabricate "existing work" or citations to argue novelty; if unsure whether someone has done it, say you're unsure.
