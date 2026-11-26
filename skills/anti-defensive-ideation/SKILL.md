---
name: anti-defensive-ideation
description: Produces bold, non-obvious ideas instead of safe incremental ones. Rules out the consensus first, generates without self-censoring, judges in a separate pass, and commits to one first pick. Use for brainstorming, research ideas, paper topics, solution concepts, and product ideas. Triggers: brainstorm, research ideas, new directions, novel ideas, think bigger, 想 idea、头脑风暴、选题、研究方向、有什么新思路.
---

# Anti-Defensive Ideation

Apply the rules and honesty floor in `../anti-defensive/SKILL.md` first.

> Generate without censoring. Judge without mercy. Then pick one.

Left alone, a model returns the most typical ideas and filters them by feasibility while it generates. The list collapses into safe increments that everyone in the field has already thought of, each with a "but this may be challenging" attached.

## Calibration

Default ideas cluster around:

- adding a module, loss, or attention variant to an existing model
- scaling up: more data, a bigger model, a longer context
- applying method A to dataset or domain B
- combining two popular methods
- wrapping it in an LLM agent, RAG, or RL fine-tuning

These aren't banned. But if every idea is one of these, you haven't started.

## Process

1. **Name the consensus.** List the 3–5 ideas anyone in the field would propose first. Don't propose them or their variants afterwards.
2. **Generate across four tiers.** No risks or feasibility at this stage.

   | Tier | Meaning |
   |---|---|
   | Incremental | a clear improvement on the current route (at most a quarter of the list) |
   | Cross-domain | a mechanism or tool borrowed from another field |
   | Contrarian | drops an assumption the field takes for granted |
   | Moonshot | if it worked, it would change how the field works |

3. **Push, then pull back.** Take promising ideas to their most radical version first, then back off to something testable. Don't start from the safe version.
4. **Judge in a separate pass.** Score value and feasibility separately, so "hard to build" doesn't drag down "matters if built". Risks belong here, not in the list.
5. **Commit.** Rank the ideas, name one first pick and why, and say what result would change your mind.

Write each idea as:

```
Name: one line
Bet: the non-obvious claim it relies on
Why now: what changed that makes it feasible
First test: the smallest experiment you can run within a week
```

## Quick checks

- Would three people in the field independently write the same list? Then diverge further.
- Is any idea a rewording of another?
- Does every idea carry "but may be challenging"? Move the risks to the judging pass.
- Is there exactly one first pick?

## Before / after

| Defensive | Anti-defensive |
|---|---|
| You could add an attention mechanism to the existing model to improve performance, though compute cost may increase. | Contrarian: remove attention. Bet: the task's dependencies are local, so convolutions plus an explicit long-range memory suffice. First test: compare on an LRA subset. |
| Here are several possible directions, each with pros and cons; the choice depends on your situation. | First pick: #3. Highest value, and its first test takes two days. #1 is safe but has a low ceiling. |

## Must keep

- In the judging pass, state fatal risks plainly: ethics, or physical or mathematical limits that make an idea infeasible.
- Don't invent prior work or citations to argue novelty. If you're not sure whether it has been done, say so.
