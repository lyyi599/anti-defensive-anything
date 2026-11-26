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
prompts/quick-prompt.md        # 无 skill 环境下的通用提示词（英文版 quick-prompt-en.md 为生成文件）
templates/SKILL.template.md    # 新增场景的模板
scripts/install.sh             # 安装
scripts/validate.py            # 校验 frontmatter 与路由表
scripts/translate.py           # 从中文源文件生成英文译文
evals/                         # 每个场景的评估用例（claude plugin eval）
.claude-plugin/                # Claude Code 插件与 marketplace 清单
.github/                       # CI 与 issue 模板
assets/                        # logo.svg、logo.png、icon.png；src/gen_logo.py 是生成脚本
CHANGELOG.md                   # 每个版本的行为变化
CLAUDE.md                      # 给 Claude 的维护约定
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
3. 在 `evals/` 下加至少一个 `<domain>-*` 用例（见下文"评估"）。
4. 如有必要，在 `prompts/quick-prompt.md` 里补一条精简规则，在 `README.md` 的使用表里补一行示例，然后运行 `python3 scripts/translate.py` 生成英文版。
5. 运行校验和该场景的评估。

每个场景 skill 都是同一套结构：**一句话原则 → 防御信号 → 规则 → 对照表 → 必须保留**。最后一节最重要：它划定了哪些防御是对的。

## 校验

```bash
python3 scripts/validate.py     # 结构、路由表、版本号、CHANGELOG、中英文同步、每个场景有评估用例
claude plugin validate .        # 插件与 marketplace 清单
```

CI（`.github/workflows/validate.yml`）在每次推送和 PR 时运行 `validate.py`，并对安装脚本做冒烟测试。

## 评估

`validate.py` 只管格式；规则有没有用，要靠评估。用例在 `evals/<场景>-<名字>/`：

```
evals/advice-db-choice/
├── prompt.md                    # 会引发防御性的请求（frontmatter: tags, runs, allowed_tools）
└── graders/
    ├── no-defensive-phrases.md  # 正则：典型防御措辞不应出现
    ├── criteria.md              # LLM 评审：反防御特征 + 诚实底线（必须保留的内容）
    └── skill-fired.md           # 指示项：skill 是否被触发（不计入与基线的对比）
```

运行：

```bash
claude plugin eval . --case 'advice-*'      # 改了哪个场景就跑哪个；默认每个用例 3 次，并跑无插件基线对比
claude plugin eval .                        # 全量
```

- 需要 git ≥ 2.31。系统 git 太旧时，可用 micromamba 装一个用户态 git，并临时加到 PATH 前面。
- skill 的对照表不能复用评估用例的内容（数据集、数字、原句），否则评估测的是照抄，不是规则。
- 每个用例都要埋一个"必须保留"的点（真实局限、边界校验、失败的测试），防止 skill 被调成一味删减或夸大。
- 正则评估的是整条回复，包括解释文字；匹配代码时要带上语法特征（例如 `except Exception\s*:`），避免误报。
- 大小写不敏感用 `flags: i`，不要写 `(?i)`（评估器用 JavaScript 正则）。
- 结果在 `evals/results/`（已 gitignore）。默认会把报告发布到 claude.ai，不想发布就加 `--no-publish`。
- 同一用例单次结果波动不小，判断改动效果时至少跑默认的 3 次。
- 开放式输出（如 ideation）的评审：一条评审只判断一件事，并写明哪些情况"不算违反"；评审模型用 `--judge-model sonnet`，默认的 haiku 在长中文输出上投票容易分裂。

新增用例时，用户反馈的 issue（"防御性案例"模板）可以直接改写成 `prompt.md` + `criteria.md`。

## 多语言

- **skill 正文只用一种语言（中文）。** 回复语言跟随用户提问的语言，与 skill 的语言无关；中英文 skill 的对比评估也没有差别。只有 `description` 里的触发词需要中英双语。
- **给人读的文档：中文是源，英文是生成的。** `README_EN.md` 和 `prompts/quick-prompt-en.md` 第一行记录了源文件和源文件哈希，不要手改。

```bash
python3 scripts/translate.py --check   # 哪些译文过时（不调用模型）
python3 scripts/translate.py           # 重新生成过时的译文（需要 claude CLI，默认用 sonnet）
python3 scripts/translate.py --force   # 全部重新生成
```

- 译文过时只是警告：`validate.py` 和 CI 会提示，但不会失败。翻译可以晚一点跟上，不会挡住改动。
- 新增需要翻译的文件：在 `scripts/translate.py` 的 `PAIRS` 里加一行（源文件、译文、目标语言）。加新语言也是同样做法。
- 文件间链接（如 `README.md` → `README_EN.md`）由脚本处理；机械替换写在脚本里，不交给模型。

## Logo

只改 `assets/src/gen_logo.py` 里的 `PARAMS`，然后运行 `python3 assets/src/gen_logo.py`，它会重新生成 `logo.svg`、`logo.png`、`icon.png`（PNG 需要 Pillow）。

## 发布

1. 在 `CHANGELOG.md` 把 `[Unreleased]` 改成新版本号和日期，写清楚每个场景行为上的变化。
2. 同步修改 `.claude-plugin/plugin.json` 和 `.claude-plugin/marketplace.json` 中的 `version`（`validate.py` 会检查两者一致且 CHANGELOG 有条目）。
3. 跑完校验和相关评估后提交并推送到 `main`，用户在 Claude Code 中更新插件即可获取新版本。
