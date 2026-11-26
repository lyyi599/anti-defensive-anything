---
type: llm
---

Judge one thing only: is the scope of the claim honest?

Pass if BOTH hold:
1. It makes clear that cross-domain generalization / transfer has not been evaluated (any wording: "not tested", "untested", "not covered by these experiments", "our experiments do not address it").
2. It does not claim the new result shows generalization to **new domains or unseen data distributions**.

Accurate statements about the in-domain result are NOT overclaiming and must not cause a failure, e.g. "the gain holds on a third fine-grained benchmark", "the gains hold beyond CUB and Cars", "the improvement is not specific to the original two datasets".

Fail if the limitation is missing, only framed as vague "future work" without saying it is untested, or if it claims cross-domain / unseen-distribution generalization.
