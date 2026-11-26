---
name: anti-defensive-coding
description: Remove defensive programming from code. Use whenever writing or changing code: writing functions, implementing features, adding features, writing scripts, fixing bugs, refactoring, reviewing code. Avoid or clean up unnecessary try/except, silent fallbacks (e.g. .get(k, default) on keys known to exist), duplicate None/type checks, unrequested compatibility layers and config options, "just in case" abstractions. Triggers: write a function, implement, add a feature, write a script, fix this bug, refactor, code review, clean up code, over-engineering, defensive programming, remove fallbacks, simplify, 写一个函数、帮我实现、加个功能、写个脚本、修一下这个 bug、重构、清理代码、过度防御、吞异常。
---

# Anti-Defensive Coding

Prerequisite: follow the core principles and honesty floor of `anti-defensive` (sibling directory `../anti-defensive/SKILL.md`).

> **Defend at the boundary, trust inside; errors should fail loudly, not be quietly swallowed.**

## Defensive signals

- `try/except` around code that can't raise, or `except Exception: pass / return None / log`
- Silently returning a default on failure, so the caller thinks it succeeded
- Re-checking with `isinstance` / `is None` what type annotations already guarantee
- Unrequested backward-compatibility layers, old parameter aliases, feature flags
- Interfaces/factories/strategy classes with only one implementation
- `.get(k, default)` on keys known to exist, turning bugs into dirty data
- Changing tests, adding skips, or loosening assertions when tests fail

## Rules

1. **Validate where the boundary is.** User input, network, files, external APIs, and process entry points get validation and error handling; internal functions trust their contracts.
2. **Only catch exceptions you can handle.** Catch only if you can recover (retry, take another path, give the user an actionable error); otherwise let it raise.
3. **No silent fallbacks.** If degradation is really needed, make it visible: a log + an explicit return status, not pretending to succeed.
4. **Assertions instead of fallbacks.** A broken internal invariant is a bug; use `assert` / raise directly so it surfaces.
5. **Don't build abstractions for hypothetical needs.** No interface before a second implementation exists; no config option nobody asked for.
6. **Minimal changes.** Fixing a bug changes only the bug, not "hardening" the surrounding code along the way.
7. **Tests protect behavior; they are not what's being protected.** When a test fails, suspect the implementation first; changing a test requires stating why.

## Before / after

```python
# Defensive
def load_config(path):
    try:
        with open(path) as f:
            data = json.load(f)
        if data is None:
            return {}
        return data.get("model", {}) if isinstance(data, dict) else {}
    except Exception:
        return {}

# Anti-defensive: a missing file or broken JSON should error, so the caller knows the config is wrong
def load_config(path: str) -> dict:
    with open(path) as f:
        return json.load(f)["model"]
```

```python
# Defensive: internal helper re-validating
def _normalize(x: np.ndarray) -> np.ndarray:
    if x is None or not isinstance(x, np.ndarray) or x.size == 0:
        return x
    return x / x.max()

# Anti-defensive
def _normalize(x: np.ndarray) -> np.ndarray:
    return x / x.max()
```

## Must keep

- Input validation and error handling at system boundaries (API handlers, CLI entry points, parsing external data).
- Resource cleanup (`with`, `finally`).
- Security-related checks: authentication, injection, path traversal, permissions.
- Real external compatibility needs (existing callers of a public API).
- Fault-tolerant behavior the user explicitly asked for.
