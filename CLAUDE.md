# CLAUDE.md

维护本仓库时的约定。项目介绍见 README.md，开发流程见 README_dev.md。

## 结构约定

- `skills/anti-defensive/` 是通用原则 + 路由表；场景 skill 在 `skills/anti-defensive-<scene>/`。
- 每个场景 skill 固定五段：一句话原则 → 防御信号 → 规则 → 对照表 → 必须保留。新增场景从 `templates/SKILL.template.md` 开始。
- 场景 skill 开头必须引用 `../anti-defensive/SKILL.md`；新增场景必须在路由表加一行，并在 `evals/` 加至少一个 `<scene>-*` 用例。

## 改动规则

- **诚实底线不能被削弱。** 反防御 ≠ 夸大：会改变决策的风险、未验证项、不知道的事必须保留。任何改动如果让 skill 更容易夸大、隐瞒或伪造，就是错的。
- 改规则 = 改模型行为。改 `skills/` 后，跑相关场景的 eval，在 `CHANGELOG.md` 的 `[Unreleased]` 下写清"哪个场景、行为上有什么变化"。
- **skill 里不能出现评估用例的内容**（数据集名、数字、原句）。对照表的例子要换领域，否则评估测的是照抄，不是规则。
- 多语言：中文文件是源，英文文件（`README_EN.md`、`prompts/quick-prompt-en.md`）由 `scripts/translate.py` 生成，**不要手改英文文件**。改完源文件运行 `python3 scripts/translate.py`；需要翻译的新文件加到脚本里的 `PAIRS`。
- skill 正文只维护中文一种语言（中英文对比评估没有差别，见 CHANGELOG 0.2.0 之后的记录）；`description` 里的触发词保持中英双语。
- 发版：同步修改 `plugin.json` 和 `marketplace.json` 的 `version`，把 `[Unreleased]` 改成版本号和日期。
- Logo 只改 `assets/src/gen_logo.py` 里的 `PARAMS`，再运行脚本生成；不要手改 `assets/logo.svg`。

## 提交前

```bash
python3 scripts/validate.py          # 会提示过时的译文
python3 scripts/translate.py         # 改了 README.md 或 quick-prompt.md 时
claude plugin validate .
claude plugin eval . --case '<scene>-*'   # 改了哪个场景就跑哪个
```
