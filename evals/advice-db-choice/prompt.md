---
tags: [advice]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

我在做一个小团队的订单管理后台：用户、订单、商品、库存之间关系很多，下单需要扣库存，不能超卖。数据量预计一年几百万行。PostgreSQL 和 MongoDB 选哪个？
