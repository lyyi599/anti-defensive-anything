---
type: regex
pattern: "^\\s+except Exception\\s*:"
flags: m
match: not_contains
---

The revised code must not contain `except Exception:` (matches indented code lines only, not explanation prose).
