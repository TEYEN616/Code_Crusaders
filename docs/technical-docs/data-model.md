---
title: Data Model
parent: Technical Docs
nav_order: 3
---

Anton Wagg
{: .label }

Tim Hötzel 
{: .label .label-green }

# Data model

## Quiz Tables 

**Questions Table:**

| id  | question | option1 | option2 | option3 | option4 | answer | answered |
| --- | -------- | ------- | ------- | ------- | ------- | ------ | -------- |
| int | text     | text    | text    | text    | text    | int    | int      |

**Users Table:**

| id  | email | username | password |
| --- | ----- | -------- | -------- |
| int | text  | text     | text     |

**Scores Table:**

| id  | user_id | score  | 
| --- | ------- | ------ |
| int | int     | int    |


