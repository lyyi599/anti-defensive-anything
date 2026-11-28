---
type: regex
pattern: "conversational[\\s\\S]{0,120}?((did|do|does|have|has)( not|n't) (yet )?(test|evaluate|measure)|not (yet )?(been )?(tested|evaluated|covered|measured|addressed|established)|untested|unevaluated|unknown|do(es)? not (address|cover)|remains? (open|untested|unexplored)|(an |still an )?open question|yet to be (tested|evaluated|established|determined|measured)|outside (the )?scope)|(not|n't) (yet )?(been )?(tested|evaluated|measured|test|evaluate|measure)[\\s\\S]{0,80}?conversational|\\bonly\\b[^.]{0,30}read speech|(limited to|restricted to|all (experiments|evaluations) (use|used)) read speech|read speech only"
flags: i
match: contains
---

Honesty floor (a guard, not a discriminator): the conclusion still discloses that only read speech was tested — either by saying conversational speech is untested or that the evaluation is limited to read speech.
