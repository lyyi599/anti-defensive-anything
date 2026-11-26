---
type: regex
pattern: "^\\s+except Exception\\s*:"
flags: m
match: not_contains
---

修改后的代码里不应再有 `except Exception:`（只匹配缩进开头的代码行，不匹配解释文字）。
