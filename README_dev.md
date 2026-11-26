# 开发者指南

面向想修改规则、新增场景或发布新版本的人。只想使用请看 [README.md](README.md)。

## 结构

```
skills/
├── anti-defensive/            # 通用原则 + 路由入口（common + router）
├── anti-defensive-writing/    # 论文、rebuttal、简历、申请书、邮件
├── anti-defensive-coding/     # 吞异常、静默 fallback、过度抽象
├── anti-defensive-ideation/   # 头脑风暴、研究 idea
├── anti-defensive-advice/     # 选型、决策、评审、反馈
└── anti-defensive-agent/      # agent 执行：过度请示、留退路的汇报
prompts/quick-prompt.md        # 无 skill 环境下的通用提示词（英文版 quick-prompt-en.md）
templates/SKILL.template.md    # 新增场景的模板
scripts/install.sh             # 安装
scripts/validate.py            # 校验 frontmatter 与路由表
.claude-plugin/                # Claude Code 插件与 marketplace 清单
```

## 工作方式

```
用户请求 ──► anti-defensive（通用原则 + 路由表）──► 加载匹配的场景 skill
                                         │
场景关键词直接命中 ──► anti-defensive-xxx ──┘ 场景 skill 先回读通用原则
```

- **两条入口都通**：每个 skill 都有自己的 `description`，Agent 会按关键词自动触发；场景 skill 开头都会引用 `../anti-defensive/SKILL.md`，所以无论从哪里进入，通用原则都会生效。
- **路由表**在 `skills/anti-defensive/SKILL.md` 里，一行一个场景：识别信号 → 加载哪个 skill。
- **诚实底线**写在通用原则里，所有场景共享：反防御 ≠ 夸大。会改变决策的风险、未验证项、不知道的事，必须保留。

## 本地开发

用软链接安装，改完文件立即生效，无需重装：

```bash
scripts/install.sh --link                       # 链接到 ~/.claude/skills
scripts/install.sh --link coding ideation       # 只链接部分场景（通用 skill 总会一起装）
scripts/install.sh --link --target ./.claude/skills   # 项目级
```

## 新增一个场景

1. 复制 `templates/SKILL.template.md` 到 `skills/anti-defensive-<domain>/SKILL.md` 并填写。
2. 在 `skills/anti-defensive/SKILL.md` 的路由表里加一行。
3. 如有必要，在 `prompts/quick-prompt.md` 和 `quick-prompt-en.md` 里补一条精简规则，在 `README.md` 和 `README_EN.md` 的使用表里补一行示例。
4. 运行校验（见下）。

每个场景 skill 都是同一套结构：**一句话原则 → 防御信号 → 规则 → 对照表 → 必须保留**。最后一节最重要：它划定了哪些防御是对的。

## 校验

```bash
python3 scripts/validate.py     # name 与目录一致、场景 skill 引用了通用原则、路由表与目录一一对应
claude plugin validate .        # 插件与 marketplace 清单
```

## 发布

1. 同步修改 `.claude-plugin/plugin.json` 和 `.claude-plugin/marketplace.json` 中的 `version`。
2. 跑完上面的校验后提交并推送到 `main`，用户在 Claude Code 中更新插件即可获取新版本。
