# Anti-Defensive Anything

**让 AI 停止"为了不出错而写"——一套轻量、零依赖的 Agent Skills。**

> 产出是为了完成目标，不是为了不被指责。

模型在很多场景都会防御：论文里提前认错，代码里到处兜底吞异常，想 idea 只敢做增量，给建议时"取决于具体情况"，执行任务时事事请示、汇报留退路。根源相同，所以用**一个通用原则 + 若干场景 skill + 一张路由表**来处理。

## 结构

```
skills/
├── anti-defensive/            # 通用原则 + 路由入口（common + router）
├── anti-defensive-writing/    # 论文、rebuttal、简历、申请书、邮件
├── anti-defensive-coding/     # 吞异常、静默 fallback、过度抽象
├── anti-defensive-ideation/   # 头脑风暴、研究 idea
├── anti-defensive-advice/     # 选型、决策、评审、反馈
└── anti-defensive-agent/      # agent 执行：过度请示、留退路的汇报
prompts/quick-prompt.md        # 无 skill 环境下的通用提示词
templates/SKILL.template.md    # 新增场景的模板
scripts/install.sh             # 安装
scripts/validate.py            # 校验 frontmatter 与路由表
.claude-plugin/                # Claude Code 插件与 marketplace 清单
```

### 怎么协作

```
用户请求 ──► anti-defensive（通用原则 + 路由表）──► 加载匹配的场景 skill
                                         │
场景关键词直接命中 ──► anti-defensive-xxx ──┘ 场景 skill 先回读通用原则
```

- **两条入口都通**：每个 skill 都有自己的 `description`，Agent 会按关键词自动触发；场景 skill 开头都会引用 `../anti-defensive/SKILL.md`，所以无论从哪里进入，通用原则都会生效。
- **路由表**在 `skills/anti-defensive/SKILL.md` 里，一行一个场景：识别信号 → 加载哪个 skill。
- **诚实底线**写在通用原则里，所有场景共享：反防御 ≠ 夸大。会改变决策的风险、未验证项、不知道的事，必须保留。

## 安装

### 方式一：Claude Code 插件（推荐）

在 Claude Code 中运行：

```
/plugin install anti-defensive-anything --marketplace lyyi599/anti-defensive-anything
```

旧版 Claude Code（2.1.275 之前）分两步：

```
/plugin marketplace add lyyi599/anti-defensive-anything
/plugin install anti-defensive-anything@lyyi599-anti-defensive
```

### 方式二：脚本安装

```bash
# Claude Code：全部安装到 ~/.claude/skills
scripts/install.sh

# 软链接安装，git pull 后自动生效
scripts/install.sh --link

# 只装部分场景（通用 skill 总会一起安装）
scripts/install.sh coding ideation

# 其他目录：Codex、项目级 skills 等
scripts/install.sh --target ~/.codex/skills
scripts/install.sh --target ./.claude/skills
```

不支持 skill 的环境：复制 [`prompts/quick-prompt.md`](prompts/quick-prompt.md) 到对话开头即可。

## 新增一个场景

1. 复制 `templates/SKILL.template.md` 到 `skills/anti-defensive-<domain>/SKILL.md` 并填写。
2. 在 `skills/anti-defensive/SKILL.md` 的路由表里加一行。
3. 运行 `python3 scripts/validate.py`，它会检查 name 与目录名是否一致、场景 skill 是否引用了通用原则、路由表与目录是否一一对应。

每个场景 skill 都是同一套结构：**一句话原则 → 防御信号 → 规则 → 对照表 → 必须保留**。最后一节最重要：它划定了哪些防御是对的。

## 致谢与相关项目

- [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)：提出"论文是发布会，不是项目总结"，是本仓库写作场景的出发点。
- [wanshuiyin/HERO-Anti-OverDefense](https://github.com/wanshuiyin/HERO-Anti-OverDefense)、[forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)：编码场景。
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)：通用文字。
- [CHATS-lab/verbalized-sampling](https://github.com/CHATS-lab/verbalized-sampling)、[jwynia/agent-skills](https://github.com/jwynia/agent-skills)：发散与 mode collapse。

## License

MIT
