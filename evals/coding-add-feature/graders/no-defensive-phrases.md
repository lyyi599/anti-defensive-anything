---
type: regex
pattern: "^[ \\t]+(try\\s*:|except\\b|.*RATES_TO_USD\\.get\\(|.*isinstance\\(|.*is None)"
flags: m
match: not_contains
---

代码行里不应出现 try/except、RATES_TO_USD.get(...)、isinstance 或 None 检查。
