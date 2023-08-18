---
title: App Behavior
parent: Technical Docs
nav_order: 2
---

Anton Wagg
{: .label }

Tim Hötzel
{: .label .label-green }

# App behavior

![Alt text](../assets/images/storyboard.JPG)
## Sign-Up and Log-In
The 'app.py'-file covers the implementation of both the user registration and the log in. The 'LoginForm' and 'SignUpForm' define 
---

## Highscore Displayment
In the route "/highscores", the high scores are retrieved from the database using the "getHighscores()" function. The highscores are then sorted in descending order based on the scores, and this sorted list of highscores is passed to the highscores.html template for rendering.

---

## Score Calculation
The user's score is calculated during the quiz interaction. In the "/quiz" route, when the user submits an answer, the code checks whether the submitted answer is correct or not. If the answer is correct, the user's score (current_score) is incremented by 1. The score is used to keep track of the user's current score during the quiz session. If the timer expires, the score can also be saved.

---

## Score Updates
The user's score is updated and saved in the database when the quiz is completed. When the user has answered all the questions or decides to exit the quiz, the "save_score(session["user_id"], current_score)" function is called to save the user's final score in the database associated with their user ID. After saving the score, the "current_score" is reset to 0 for the next quiz session.

---

## Highscore DB Updates
The highscores are updated in the database whenever a user completes the quiz. The "save_score(user_id, score)" function inserts a new record into the scores table, associating the user's ID with their score. This information is then used to display high scores in the /highscores route. (Only if you are logged in)

---



