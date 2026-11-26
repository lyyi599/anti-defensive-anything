---
name: anti-defensive-coding
description: 去除代码中的防御性编程。只要要写或改代码就使用：写函数、实现功能、加功能、写脚本、修 bug、重构、审查代码。避免或清理多余的 try/except、静默 fallback（如对已知存在的 key 用 .get(k, default)）、重复的空值/类型检查、未被要求的兼容层和配置项、"以防万一"的抽象。触发：写一个函数、帮我实现、加个功能、写个脚本、修一下这个 bug、重构、code review、清理代码、过度防御、吞异常、write a function、implement、add a feature、fix this bug、refactor、over-engineering、defensive programming、remove fallbacks、simplify。
---

# Anti-Defensive Coding

前置：遵循 `anti-defensive` 的通用原则与诚实底线（同级目录 `../anti-defensive/SKILL.md`）。

> **在边界防御，在内部信任；错误要大声失败，不要被悄悄吞掉。**

## 防御信号

- `try/except` 包着不会抛异常的代码，或 `except Exception: pass / return None / log`
- 失败时静默返回默认值，让调用方以为成功了
- 类型注解已保证的内容又做一遍 `isinstance` / `is None` 检查
- 没人要求的向后兼容层、旧参数别名、feature flag
- 只有一个实现的接口/工厂/策略类
- 对已知存在的 key 用 `.get(k, default)`，把 bug 变成脏数据
- 测试失败时改测试、加 skip、放宽断言

## 规则

1. **边界在哪里，校验就在哪里。** 用户输入、网络、文件、外部 API、进程入口要校验和处理错误；内部函数之间信任契约。
2. **只捕获你能处理的异常。** 能恢复（重试、换路径、给用户可行动的报错）才 catch；否则让它抛出。
3. **不要静默 fallback。** 如果确实需要降级，必须可见：日志 + 明确的返回状态，而不是假装成功。
4. **断言代替兜底。** 内部不变量被破坏是 bug，用 `assert` / 直接抛错让它暴露。
5. **不为假想需求建抽象。** 第二个实现出现之前不建接口；没人要求就不加配置项。
6. **最小改动。** 修 bug 只改 bug，不顺手"加固"周边代码。
7. **测试保护行为，不是被保护的对象。** 测试失败先怀疑实现；改测试必须说明理由。

## 对照

```python
# 防御性
def load_config(path):
    try:
        with open(path) as f:
            data = json.load(f)
        if data is None:
            return {}
        return data.get("model", {}) if isinstance(data, dict) else {}
    except Exception:
        return {}

# 反防御：文件不存在或 JSON 坏了就该报错，调用方才知道配置有问题
def load_config(path: str) -> dict:
    with open(path) as f:
        return json.load(f)["model"]
```

```python
# 防御性：内部 helper 重复校验
def _normalize(x: np.ndarray) -> np.ndarray:
    if x is None or not isinstance(x, np.ndarray) or x.size == 0:
        return x
    return x / x.max()

# 反防御
def _normalize(x: np.ndarray) -> np.ndarray:
    return x / x.max()
```

## 必须保留

- 系统边界的输入校验和错误处理（API handler、CLI 入口、解析外部数据）。
- 资源清理（`with`、`finally`）。
- 安全相关检查：鉴权、注入、路径穿越、权限。
- 真实存在的外部兼容需求（公开 API 的已有调用方）。
- 用户明确要求的容错行为。
