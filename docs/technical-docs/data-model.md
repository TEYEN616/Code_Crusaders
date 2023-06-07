---
title: Data Model
parent: Technical Docs
nav_order: 3
---

Anton Wagg
{: .label }

# Data model
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## User related Tables 

**User:**
|  #user_ID fk| username  | password | confirm_password|
| --------    | --------  | -------- | --------|
|  int        | String    | String   | String  |


**Results:**
| #user_ID | #score   | 
| -------- | -------- | 
| int      | int      | 

---
## Quiz Questions

**Questions:**
|  question_ID | question | answer_a | answer_b| answer_c | answer_d|
| -------- | -------- | -------- | -------- | ------- | -------|
| int      | string   | string   | string   | string  | string |
