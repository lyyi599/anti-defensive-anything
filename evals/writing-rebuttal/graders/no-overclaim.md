---
type: regex
pattern: "generaliz\\w*\\s+(\\w+\\s+){0,3}(to|across)\\s+(new|unseen|other|different)\\s+(domains?|data|distributions?)|(to|across) (new|unseen) domains?"
flags: i
match: not_contains
---

The reply must not claim generalization to new domains or unseen data from an in-domain result.
