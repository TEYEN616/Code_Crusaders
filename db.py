import random
import sqlite3

from flask import current_app, g


def checkUser(username, password):
        conn = sqlite3.connect("quiz.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username= ? AND password= ?",
            (username, password),
        )
        user = cursor.fetchone()
        conn.close()

        return user


def insert_user(email, username, password):
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (email, username, password) VALUES (?, ?, ?)",
        (email, username, password),
    )
    conn.commit()
    conn.close()

    # ? = placeholder
    # insert into users: values stored user.db with sql statement


def reset_quiz():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    # Markierung der beantworteten Fragen entfernen
    cursor.execute("UPDATE questions SET answered = 0")
    conn.commit()

    # Verbindung zur Datenbank schließen
    conn.close()


def save_score(user_id, score):
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    # Punktestand in der Datenbank speichern
    cursor.execute(
        "INSERT INTO scores (user_id, score) VALUES (?, ?)", (user_id, score)
    )
    conn.commit()

    conn.close()


def getNextQuestion(questions):
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    question = random.choice(questions)

    # Frage als beantwortet markieren
    cursor.execute("UPDATE questions SET answered = 1 WHERE id = ?", (question[0],))
    conn.commit()

    conn.close()

    return question


def getUnansweredQuestions():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM questions WHERE answered = 0")
    conn.commit()
    
    questions = cursor.fetchall()
    conn.close()
    

    return questions


def getQuestion(question_id):
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM questions WHERE id = ?", (question_id,))
    conn.commit()

    question = cursor.fetchone()
    conn.close()

    return question

def getHighscores():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT username, MAX(score) FROM users JOIN scores ON users.id = scores.user_id GROUP BY users.id"
    )
    conn.commit()
    high_scores = cursor.fetchall()
    
    conn.close()

    return high_scores
    
