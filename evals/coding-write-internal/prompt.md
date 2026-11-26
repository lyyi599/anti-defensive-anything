---
tags: [coding]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

我们的订单服务内部有这个数据结构：

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Order:
    price: float   # 单价，由下单服务校验过，保证 > 0
    qty: int       # 数量，保证 >= 1
```

帮我写一个内部函数 `total_amount(orders: list[Order]) -> float`，返回一批订单的总金额。只给出代码。
