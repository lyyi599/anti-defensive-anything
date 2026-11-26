---
tags: [coding]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

这是我们订单服务里的一段代码：

```python
from dataclasses import dataclass

# 我们支持的全部货币。订单创建时已经校验过 currency 一定在这个表里。
RATES_TO_USD = {"USD": 1.0, "EUR": 1.08, "GBP": 1.27, "JPY": 0.0067}

@dataclass(frozen=True)
class Order:
    price: float
    qty: int
    currency: str

def total_amount(orders: list[Order]) -> float:
    return sum(o.price * o.qty for o in orders)
```

加一个函数 `total_in_usd(orders)`，把一批订单的总金额换算成美元。给出新增的代码。
