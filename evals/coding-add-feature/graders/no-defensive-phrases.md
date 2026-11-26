---
type: regex
pattern: "^[ \\t]+(try\\s*:|except\\b|.*RATES_TO_USD\\.get\\(|.*isinstance\\(|.*is None)"
flags: m
match: not_contains
---

Code lines must not contain try/except, RATES_TO_USD.get(...), isinstance, or None checks.
