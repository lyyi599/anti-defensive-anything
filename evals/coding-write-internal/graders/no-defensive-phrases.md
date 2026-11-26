---
type: regex
pattern: "^[ \\t]+(try\\s*:|except\\b|.*isinstance\\(|.*is None)"
flags: m
match: not_contains
---

The internal function must not contain try/except, isinstance, or None checks (code lines only).
