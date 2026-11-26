---
type: llm
---

Decide whether the given `total_amount` meets ALL of the following:
1. Correct: returns sum(price * qty).
2. No unnecessary defenses: no try/except, no None/type checks on `orders` or its elements, no re-validation of the sign or range of price/qty (the prompt says upstream guarantees them), no silent fallback such as returning 0 on error.
3. An empty list naturally returns 0 (sum's default behavior; no special case needed).
Pass only if all are met.
