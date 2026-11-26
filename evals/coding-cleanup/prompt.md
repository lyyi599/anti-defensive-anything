---
tags: [coding]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

帮我清理下面这段 Python 代码里多余的防御性写法，直接给出修改后的完整代码：

```python
from flask import Flask, request, jsonify
app = Flask(__name__)

def _scale(values: list[float], factor: float) -> list[float]:
    try:
        if values is None or not isinstance(values, list):
            return []
        if factor is None:
            factor = 1.0
        return [v * factor for v in values]
    except Exception:
        return []

@app.post("/scale")
def scale_endpoint():
    payload = request.get_json(silent=True)
    if not payload or "values" not in payload:
        return jsonify(error="missing 'values'"), 400
    try:
        values = [float(v) for v in payload["values"]]
        factor = float(payload.get("factor", 1.0))
    except (TypeError, ValueError):
        return jsonify(error="values and factor must be numbers"), 400
    return jsonify(result=_scale(values, factor))
```
