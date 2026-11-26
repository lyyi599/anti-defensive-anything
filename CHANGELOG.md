# Changelog

版本号同时写在 `.claude-plugin/plugin.json` 和 `.claude-plugin/marketplace.json`，`scripts/validate.py` 会检查两者一致，并要求这里有对应条目。

规则改动会直接改变模型行为，所以每条记录写清楚**哪个场景、行为上有什么变化**。

## [Unreleased]

### Changed
- `agent`：触发描述覆盖"写最终汇报 / 进度更新 / 修复说明"。此前这类请求不会触发 skill；修改后 `agent-report` 3/3 触发，得分 1.00（无插件基线 0.67）。
- `advice`：触发描述覆盖"A 还是 B / 选哪个 / 该不该"等选择类问题。此前不会触发；修改后 `advice-db-choice` 3/3 触发，得分 1.00（无插件基线 0.50）。

- `writing`：rebuttal 规则明确"第一句就是回应本身，不以 thank/apologize 开头"，并要求新证据只主张它实际覆盖的范围（同领域新数据集 ≠ 新领域）。此前 2 次中 1 次以感谢开头并夸大泛化范围；修改后 `writing-rebuttal` 5/5 通过（无插件基线 0/5）。

## [0.1.0] - 2026-11-26

### Added
- 通用原则与路由 skill `anti-defensive`，含诚实底线。
- 场景 skill：`writing`、`coding`、`ideation`、`advice`、`agent`。
- 中英文通用提示词、新场景模板、安装与校验脚本。
- Claude Code 插件与 marketplace 清单。
- Logo（星冲破盾）及其生成脚本 `assets/src/gen_logo.py`。
- 每个场景的评估用例（`evals/`），用 `claude plugin eval` 运行。
- CI：推送和 PR 时运行 `scripts/validate.py`。
