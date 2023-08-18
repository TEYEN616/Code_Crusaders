---
title: App Structure
parent: Technical Docs
nav_order: 1
---

Anton Wagg
{: .label }

Tim Hötzel 
{: .label .label-green }

# App structure

## File Organisation

<pre><code>ProjectDirectory/
│
├── app.py
├── app.py
├── db.py
├── fragen.py
├── requirements.txt
├── README.txt
├── .gitignore
├── quiz.db
├── static/
│   ├── css/
│       └── style.css
└── templates/
    ├── login-page.html
    ├── signup.html
    ├── homepage.html
    ├── quiz.html
    ├── gkQuiz.html
    └── highscores.html

</code></pre>

## Login/ Register

## GeneralKnowledge
The general knowledge mode offers questions from various subject areas and is used to improve general knowledge. There is no timer and correct questions are not counted as points.

## Rush
Rush mode offers timed playback of questions, when time runs out the quiz is over. The quiz also ends when all questions have been answered. The correctly answered questions give a point and are added to the high score at the end if it is higher than the old one.

#### Not developed:  
This mode would combine all questions of the area when implementing topic-specific subjects with subcategories. It would be more challenging because you would have to be familiar with the whole subject area.

## Highscore
Highscores is a small approach to multiplayer usage. It always shows the highest  score of the respective user. Consistent with our value proposition challenge and competition. The high score motivates the player to try harder and also to outbid his friends.