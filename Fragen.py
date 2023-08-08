import sqlite3

conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS questions (
                    id INTEGER PRIMARY KEY,
                    question TEXT,
                    option1 TEXT,
                    option2 TEXT,
                    option3 TEXT,
                    option4 TEXT,
                    answer INTEGER,
                    answered INTEGER DEFAULT 0
                )"""
)
# Tabelle für user erstellen
cursor.execute(
    """
                   CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   email TEXT NOT NULL,
                   username TEXT NOT NULL,
                   password TEXT NOT NULL
                    )
                   """
)


# Neu -----------------------------------------
cursor.execute(
    """CREATE TABLE IF NOT EXISTS scores (
                    id INTEGER PRIMARY KEY,
                    score INTEGER
                )"""
)
# Neu -----------------------------------------
questions = [
    {
        "id": 1,
        "question": "Wie heißt die Hauptstadt von Frankreich?",
        "option1": "Madrid",
        "option2": "Paris",
        "option3": "Berlin",
        "option4": "London",
        "answer": 2,
    },
    {
        "id": 2,
        "question": "Wie viele Planeten hat unser Sonnensystem?",
        "option1": "7",
        "option2": "8",
        "option3": "9",
        "option4": "10",
        "answer": 2,
    },
    {
        "id": 3,
        "question": "Was ist die Hauptstadt von Kanada?",
        "option1": "Ottawa",
        "option2": "Toronto",
        "option3": "Montreal",
        "option4": "Vancouver",
        "answer": 1,
    },
    {
        "id": 4,
        "question": "Wie viele Kontinente gibt es auf der Erde??",
        "option1": "5",
        "option2": "6",
        "option3": "7",
        "option4": "8",
        "answer": 3,
    },
    {
        "id": 5,
        "question": "Wie viele Milliliter sind in einem Liter?",
        "option1": "100",
        "option2": "500",
        "option3": "1000",
        "option4": "2000",
        "answer": 3,
    },
    {
        "id": 6,
        "question": "Wie viele Elemente enthält das Periodensystem",
        "option1": "98",
        "option2": "105",
        "option3": "118",
        "option4": "124",
        "answer": 3,
    },
]

for question in questions:
    cursor.execute(
        """INSERT INTO questions (id, question, option1, option2, option3, option4, answer, answered)
                      VALUES (?, ?, ?, ?, ?, ?, ?, 0)""",
        (
            question["id"],
            question["question"],
            question["option1"],
            question["option2"],
            question["option3"],
            question["option4"],
            question["answer"],
        ),
    )

conn.commit()
conn.close()
