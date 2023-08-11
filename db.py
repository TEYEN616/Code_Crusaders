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


def initialize_score():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    # Tabelle 'scores' erstellen, wenn sie nicht existiert
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS scores (
                        id INTEGER PRIMARY KEY,
                        score INTEGER DEFAULT 0
                    )"""
    )

    # Prüfen, ob bereits ein Eintrag in der Tabelle vorhanden ist
    cursor.execute("SELECT * FROM scores")
    existing_score = cursor.fetchone()

    if not existing_score:
        # Kein Eintrag vorhanden, wir setzen den Punktestand auf 0
        cursor.execute("INSERT INTO scores (score) VALUES (?)", (0,))
        conn.commit()

    conn.close()


# Score aktualisieren
def update_score():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    # Punktestand aus der Datenbank abrufen
    cursor.execute("SELECT score FROM scores")
    current_score = cursor.fetchone()

    if current_score:
        # Punktestand erhöhen
        score = current_score[0] + 1

        # Punktestand in der Datenbank aktualisieren
        cursor.execute("UPDATE scores SET score = ?", (score,))
        conn.commit()

    conn.close()
