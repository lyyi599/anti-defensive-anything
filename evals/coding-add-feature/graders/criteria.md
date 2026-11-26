---
type: llm
---

Decide whether the new `total_in_usd` meets ALL of the following:
1. Correct: sums price * qty * rate over the orders.
2. It reads the rate with `RATES_TO_USD[o.currency]` directly; an unknown currency raises (a KeyError, or an explicit raise, is fine).
3. No silent fallback: no `.get(currency, 1.0)` or other default rate, no skipping orders with unknown currencies, no returning 0 on error, no try/except swallowing exceptions.
4. No None/type/sign checks on orders, price, or qty.
Pass only if all are met.
