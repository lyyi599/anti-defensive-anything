---
type: regex
pattern: "^[ \\t]+(try\\s*:|except\\b|.*isinstance\\(|.*is None)"
flags: m
match: not_contains
---

内部函数里不应出现 try/except、isinstance 或 None 检查。
