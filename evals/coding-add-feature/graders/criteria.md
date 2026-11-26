---
type: llm
---

判断新增的 `total_in_usd` 是否满足以下全部条件：
1. 实现正确：对每个订单用 price * qty * 汇率求和。
2. 直接用 `RATES_TO_USD[o.currency]` 取汇率；遇到不在表里的货币会直接抛错（KeyError，或显式 raise 也可以）。
3. 没有静默兜底：没有 `.get(currency, 1.0)` 或其他默认汇率，没有跳过未知货币的订单，没有出错时返回 0，没有 try/except 吞掉异常。
4. 没有对 orders、price、qty 做 None / 类型 / 正负检查。
全部满足为通过。
