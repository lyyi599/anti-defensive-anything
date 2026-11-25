# Anti-Defensive Anything

**让 AI 停止"为了不出错而写"——一套轻量、零依赖的 Agent Skills。**

> 产出是为了完成目标，不是为了不被指责。

论文里提前认错、代码里到处兜底吞异常、想 idea 只敢做增量、给建议"取决于具体情况"、执行任务事事请示——装上之后，AI 在这些场景里直接给结论、做取舍、把事做完；真正会影响你决策的风险照样说清楚。

## 安装

**Claude Code（推荐）**：在 Claude Code 中运行

```
/plugin install anti-defensive-anything --marketplace lyyi599/anti-defensive-anything
```

<details>
<summary>旧版 Claude Code（2.1.275 之前）</summary>

```
/plugin marketplace add lyyi599/anti-defensive-anything
/plugin install anti-defensive-anything@lyyi599-anti-defensive
```
</details>

**Codex / 其他 Agent 工具**：

```bash
git clone https://github.com/lyyi599/anti-defensive-anything.git
cd anti-defensive-anything
scripts/install.sh --target ~/.codex/skills   # 不加 --target 则装到 ~/.claude/skills
```

**网页版对话 / 不支持 skill 的工具**：把 [`prompts/quick-prompt.md`](prompts/quick-prompt.md) 粘贴到对话开头。

## 使用

装好后正常提需求即可，会按场景自动生效：

| 场景 | 例如这样说 |
|---|---|
| 写作 | "帮我润色这段摘要""写 rebuttal""改一下简历" |
| 编码 | "重构这个模块""review 这段代码""清理一下过度防御" |
| 想法 | "围绕 X 头脑风暴几个研究 idea" |
| 建议 | "PostgreSQL 还是 MongoDB？""直说，这个方案行不行" |
| 执行 | "直接做完，别老问我" |

任何场景里觉得 AI 又开始含糊了，说一句"别那么防御"即可。

## 致谢与相关项目

- [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)
- [wanshuiyin/HERO-Anti-OverDefense](https://github.com/wanshuiyin/HERO-Anti-OverDefense)
- [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)
- [CHATS-lab/verbalized-sampling](https://github.com/CHATS-lab/verbalized-sampling)
- [jwynia/agent-skills](https://github.com/jwynia/agent-skills)

## License

MIT · 想修改规则或新增场景，见 [README_dev.md](README_dev.md)
