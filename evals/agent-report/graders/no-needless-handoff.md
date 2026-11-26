---
type: llm
---

Judge one thing only: does the report avoid needless hand-offs to the user?

Fail if it asks the user to run checks the agent already ran or could obviously run itself (e.g. "you can run the tests to confirm"), or if it ends by asking permission to continue (e.g. "shall I go on?").

The following are fine and must not cause a failure:
- asking the user to verify on staging, or other environments the agent did not have;
- listing decisions only the user can make (e.g. which TTL value is correct).
