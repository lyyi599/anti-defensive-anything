<p align="center"><img src="assets/logo.svg" width="180" alt="Anti-Defensive Anything logo"></p>

# Anti-Defensive Anything

[中文](README.md) · English

**Stop AI from writing to avoid blame — a lightweight, zero-dependency set of Agent Skills.**

> Output exists to get the job done, not to avoid being blamed.

Papers that apologize before reviewers say a word, code wrapped in fallbacks that swallow errors, research ideas that never leave incremental territory, advice that ends in "it depends", agents that ask permission for every step. With these skills installed, the AI leads with conclusions, makes trade-offs, and finishes the work — while still stating the risks that would change your decision.

## Install

**Claude Code (recommended)** — run inside Claude Code:

```
/plugin install anti-defensive-anything --marketplace lyyi599/anti-defensive-anything
```

<details>
<summary>Older Claude Code (before 2.1.275)</summary>

```
/plugin marketplace add lyyi599/anti-defensive-anything
/plugin install anti-defensive-anything@lyyi599-anti-defensive
```
</details>

**Codex / other agent tools**:

```bash
git clone https://github.com/lyyi599/anti-defensive-anything.git
cd anti-defensive-anything
scripts/install.sh --target ~/.codex/skills   # without --target, installs to ~/.claude/skills
```

**Web chat / tools without skill support**: paste [`prompts/quick-prompt-en.md`](prompts/quick-prompt-en.md) at the start of the conversation.

> The skill files are written in Chinese. Models apply them to English tasks without issue, and replies follow the language you use.

## Usage

Just ask as usual; the matching skill kicks in automatically:

| Scenario | Say something like |
|---|---|
| Writing | "Polish this abstract", "Draft the rebuttal", "Tighten my resume" |
| Coding | "Refactor this module", "Review this code", "Remove the over-defensive checks" |
| Ideation | "Brainstorm research ideas around X" |
| Advice | "PostgreSQL or MongoDB?", "Be blunt — will this design work?" |
| Agent tasks | "Just finish it, don't keep checking in" |

Whenever the AI starts hedging again, say "stop being defensive".

## Acknowledgements & related projects

- [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)
- [wanshuiyin/HERO-Anti-OverDefense](https://github.com/wanshuiyin/HERO-Anti-OverDefense)
- [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)
- [CHATS-lab/verbalized-sampling](https://github.com/CHATS-lab/verbalized-sampling)
- [jwynia/agent-skills](https://github.com/jwynia/agent-skills)

## License

MIT · To change rules or add a scenario, see [README_dev.md](README_dev.md) (Chinese)
