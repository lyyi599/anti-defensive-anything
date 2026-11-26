# Changelog

版本号同时写在 `.claude-plugin/plugin.json` 和 `.claude-plugin/marketplace.json`，`scripts/validate.py` 会检查两者一致，并要求这里有对应条目。

规则改动会直接改变模型行为，所以每条记录写清楚**哪个场景、行为上有什么变化**。

## [Unreleased]

### Known issues（首轮评估发现，每个用例只跑了 1 次）
- `agent`：给出"写最终汇报"这类请求时 skill 没有被触发；description 的触发词偏向"别老问我"。
- `advice`：用户只问"A 和 B 选哪个"时 skill 没有被触发。
- `writing`：rebuttal 有时仍以 "We thank the reviewer" 开头，并把同领域新数据集的结果说成"在未见数据上也成立"（2 次中 1 次）。

## [0.1.0] - 2026-11-26

### Added
- 通用原则与路由 skill `anti-defensive`，含诚实底线。
- 场景 skill：`writing`、`coding`、`ideation`、`advice`、`agent`。
- 中英文通用提示词、新场景模板、安装与校验脚本。
- Claude Code 插件与 marketplace 清单。
- Logo（星冲破盾）及其生成脚本 `assets/src/gen_logo.py`。
- 每个场景的评估用例（`evals/`），用 `claude plugin eval` 运行。
- CI：推送和 PR 时运行 `scripts/validate.py`。
