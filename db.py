import sqlite3

from flask import current_app, g


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
