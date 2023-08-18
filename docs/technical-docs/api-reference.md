---
title: API Reference
parent: Technical Docs
nav_order: 4
---

Tim Hötzel 
{: .label .label-green }

# API reference Index Screenshots hinzufügen

## Navigation  

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
![Alt text](../assets/images/login.JPG)



## Login / Sign Up

### `signup()`

**Route:** `/signup`

**Methods:** `POST` `GET`

**Purpose:** Non-existing users can register and then log in. User data is stored in the database.

**Sample output:**
Shows a registration form.
![Alt text](../assets/images/signUp.jpg)

## Navigation / Homepage

### `homepage()`

**Route:** `/homepage`

**Methods:** `POST` `GET`

**Purpose:** Choice between the two implemented game modes

**Sample output:**
Two buttons with Rush and General Knowledge
![Alt text](../assets/images/homepage.jpg)


## Quiz / Rush

### `quiz()`

**Route:** `/quiz`

**Methods:** `POST` `GET`

**Purpose:** gameloop

**Sample output:**
Shows a question, timer, score, answer button and whether the question was answered correctly or incorrectly.
![Alt text](../assets/images/rush.jpg)


## Quiz / General knowlage

### `gkquiz()`

**Route:** `/gkquiz`

**Methods:** `POST` `GET`

**Purpose:** gameloop

**Sample output:**
Shows a question, answer button and whether the question was answered correctly or incorrectly.
![Alt text](../assets/images/generalKnowlage.JPG)

## Highscore

### `highscore()`

**Route:** `/highscore`

**Methods:** `POST` `GET`

**Purpose:** List of high scores

**Sample output:**
Table with user entries and their highest score.
![Alt text](../assets/images/highscores.jpg)


