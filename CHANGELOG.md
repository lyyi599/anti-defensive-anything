# Changelog

版本号同时写在 `.claude-plugin/plugin.json` 和 `.claude-plugin/marketplace.json`，`scripts/validate.py` 会检查两者一致，并要求这里有对应条目。

规则改动会直接改变模型行为，所以每条记录写清楚**哪个场景、行为上有什么变化**。

## [Unreleased]

### Added
- `scripts/translate.py`：英文文档（`README_EN.md`、`prompts/quick-prompt-en.md`）改为从中文源文件生成，译文首行记录源文件哈希；过时的译文由 `validate.py` 警告，不阻塞 CI。

### Changed
- `validate.py`：去掉逐项比对中英文 README 行数的硬性检查，改为译文过时警告。
- README 注明 skill 正文为中文、对英文请求同样有效。依据：同一批评估用例上，中文 skill 触发 18/23、质量评审 55/55；完整翻译的英文 skill 触发 14/21、质量评审 50/51，没有体现出英文更好，因此 skill 保持中文单语。

## [0.2.0] - 2026-11-26

### Changed
- `agent`：触发描述覆盖"写最终汇报 / 进度更新 / 修复说明"。此前这类请求不会触发 skill；修改后 `agent-report` 3/3 触发，得分 1.00（无插件基线 0.67）。
- `advice`：触发描述覆盖"A 还是 B / 选哪个 / 该不该"等选择类问题。此前不会触发；修改后 `advice-db-choice` 3/3 触发，得分 1.00（无插件基线 0.50）。
- `writing`：rebuttal 规则明确"第一句就是回应本身，不以 thank/apologize 开头"，并要求新证据只主张它实际覆盖的范围（同领域新数据集 ≠ 新领域）。此前 2 次中 1 次以感谢开头并夸大泛化范围；修改后 `writing-rebuttal` 5/5 通过（无插件基线 0/5）。
- `coding`：触发描述覆盖"写函数 / 实现 / 加功能 / 修 bug"等普通编码请求。
- 评估：`ideation-research` 的综合评审拆成 4 个单项（大胆 idea / 首选 / 列表不挂保留话 / 不编造），改用 sonnet 评审后 3 票一致：有插件 1.00，无插件 0.60（基线 3/3 没有非增量 idea）。新增 `coding-add-feature` 用例。

### Known issues
- `coding`：三个用例（清理代码、写内部函数、给已有代码加功能）无插件基线都是满分，当前模型在这类小任务上本身就不防御，测不出 skill 的作用。补了触发词后 skill 仍很少被调用（两个用例 6 次中 1 次）。用例保留作回归防护。

## [0.1.0] - 2026-11-26

### Added
- 通用原则与路由 skill `anti-defensive`，含诚实底线。
- 场景 skill：`writing`、`coding`、`ideation`、`advice`、`agent`。
- 中英文通用提示词、新场景模板、安装与校验脚本。
- Claude Code 插件与 marketplace 清单。
- Logo（星冲破盾）及其生成脚本 `assets/src/gen_logo.py`。
- 每个场景的评估用例（`evals/`），用 `claude plugin eval` 运行。
- CI：推送和 PR 时运行 `scripts/validate.py`。
