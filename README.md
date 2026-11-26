<div align="center">

<img src="assets/logo.svg" width="160" alt="Anti-Defensive Anything logo">

# Anti-Defensive Anything

**Stop AI from writing to avoid blame.**<br>
A lightweight, zero-dependency set of Agent Skills for writing and ideation.

[![CI](https://github.com/lyyi599/anti-defensive-anything/actions/workflows/validate.yml/badge.svg)](https://github.com/lyyi599/anti-defensive-anything/actions/workflows/validate.yml)
[![Version](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Flyyi599%2Fanti-defensive-anything%2Fmain%2F.claude-plugin%2Fplugin.json&query=%24.version&label=version&color=E4573D)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-D97757)](#install)

<a href="#install">Install</a> · <a href="#usage">Usage</a> · <a href="#what-changes">What changes</a> · <a href="README_dev.md">Develop</a><br>
English · <a href="README_CN.md">中文</a>

</div>

<br>

> [!NOTE]
> Output exists to get the job done, not to avoid being blamed.

Papers that apologize before reviewers say a word. Rebuttals that open with three sentences of thanks. Brainstorms that never leave incremental territory. With these skills installed, the AI **leads with the point**, **commits to a first pick**, and **keeps every real limitation**, stated plainly.

## What changes

<table>
<tr><th width="50%">Before</th><th width="50%">After</th></tr>
<tr>
<td><i>Although our compiler pass cuts latency on two ARM boards, we must admit we have not measured it on GPUs, so the results should be viewed with caution.</i></td>
<td>Our compiler pass cuts latency on two ARM boards; GPU performance has not been measured.</td>
</tr>
<tr>
<td><i>Participated in optimizing the recommendation system, with some positive results.</i></td>
<td>Rewrote the retrieval module; online CTR +4.2%.</td>
</tr>
<tr>
<td><i>Five ideas, all "add a module" or "scale it up", each ending with "this may be worth exploring".</i></td>
<td>Ideas across four tiers, from incremental to moonshot, each with a bet and a first test, and one first pick.</td>
</tr>
</table>

Measured with `claude plugin eval` (3 runs per arm, Chinese prompts):

| Case | Check | With skills | Without |
|---|---|:---:|:---:|
| Rebuttal | Opens with the response, not thanks | **3/3** | 0/3 |
| Rebuttal | Keeps the untested limitation | **3/3** | 1/3 |
| Conclusion | Ends on the takeaway | **3/3** | 0/3 |
| Research ideas | At least one non-incremental idea | **3/3** | 0/3 |

## Install

**Claude Code (recommended)**: run inside Claude Code

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

<details>
<summary>Codex / other agent tools</summary>

```bash
git clone https://github.com/lyyi599/anti-defensive-anything.git
cd anti-defensive-anything
scripts/install.sh --target ~/.codex/skills   # without --target, installs to ~/.claude/skills
```
</details>

<details>
<summary>Web chat / tools without skill support</summary>

Paste [`prompts/quick-prompt.md`](prompts/quick-prompt.md) at the start of the conversation.
</details>

> [!TIP]
> The skills are written in English and trigger on both English and Chinese requests; replies follow the language you write in.

## Usage

Just ask as usual; the matching skill kicks in automatically.

| Skill | Say something like |
|---|---|
| ✍️ **Writing** | "Polish this abstract", "Rewrite this rebuttal paragraph", "Tighten my resume" |
| 💡 **Ideation** | "Brainstorm research ideas around X", "Give me bolder directions for this project" |

Whenever the AI starts hedging again, say **"stop being defensive"**.

## Acknowledgements

- [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)
- [wanshuiyin/HERO-Anti-OverDefense](https://github.com/wanshuiyin/HERO-Anti-OverDefense)
- [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)
- [CHATS-lab/verbalized-sampling](https://github.com/CHATS-lab/verbalized-sampling)
- [jwynia/agent-skills](https://github.com/jwynia/agent-skills)

## License

[MIT](LICENSE). To change rules or add a scenario, see [README_dev.md](README_dev.md).
