---
title: API Reference
parent: Technical Docs
nav_order: 4
---

Tim Hötzel 
{: .label .label-green }

# API reference

## Navigation / Index

### `index()`

**Route:** `/`

**Methods:** `POST` `GET` 

**Purpose:** [Short explanation of what the function does and why]

**Sample output:** NONE


## Login / Login

### `logIn()`

**Route:** `/logIn`

**Methods:** `POST` `GET`

**Purpose:** Login for existing users and forwarding to register

**Sample output:**
Shows the login screen with input fields for the registration and a SignUp button.



## Login / Register

### `signup()`

**Route:** `/signup`

**Methods:** `POST` `GET`

**Purpose:** [Short explanation of what the function does and why]

**Sample output:**

Shows a registration form.


## Navigation / Subjects

### `homepage_subjects()`

**Route:** `/homepage_subjects`

**Methods:** `POST` `GET`

**Purpose:** (Select subjects for specific learning)

**Sample output:**

Shows a few buttons as a subject selection


## Navigation / Mode selection

### `homepage()`

**Route:** `/homepage`

**Methods:** `POST` `GET`

**Purpose:** Choice between the two implemented game modes

**Sample output:**

Two buttons with Rush and General Knowledge


## Quiz / Rush

### `quiz()`

**Route:** `/quiz`

**Methods:** `POST` `GET`

**Purpose:** gameloop

**Sample output:**

Shows a question, timer, score, answer button and whether the question was answered correctly or incorrectly.


## Quiz / General knowlage

### `gkquiz()`

**Route:** `/gkquiz`

**Methods:** `POST` `GET`

**Purpose:** gameloop

**Sample output:**

Shows a question, answer button and whether the question was answered correctly or incorrectly.


## Highscore

### `highscore()`

**Route:** `/highscore`

**Methods:** `POST` `GET`

**Purpose:** List of high scores

**Sample output:**

Table with user entries and their highest score.


