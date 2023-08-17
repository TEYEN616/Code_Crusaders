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
                        user_id INTEGER,
                        score INTEGER DEFAULT 0,
                        FOREIGN KEY (user_id) REFERENCES users (id)
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
    {
        "id": 7,
        "question": "Was ist die Hauptkomponente der Luft?",
        "option1": "Kohlenstoffdioxid",
        "option2": "Sauerstoff",
        "option3": "Stickstoff",
        "option4": "Wasserstoff",
        "answer": 3,
    },
    {
        "id": 8,
        "question": "Welcher Planet ist der drittgrößte in unserem Sonnensystem?",
        "option1": "Mars",
        "option2": "Venus",
        "option3": "Jupiter",
        "option4": "Saturn",
        "answer": 2,
    },
    {
        "id": 9,
        "question": "Was ist die chemische Formel für Wasser?",
        "option1": "H2O2",
        "option2": "CO2",
        "option3": "H2O",
        "option4": "O2",
        "answer": 3,
    },
    {
        "id": 10,
        "question": "Wie wird die Einheit der elektrischen Spannung genannt?",
        "option1": "Ampere",
        "option2": "Ohm",
        "option3": "Watt",
        "option4": "Volt",
        "answer": 4,
    },
    {
        "id": 11,
        "question": "Was ist die chemische Bezeichnung für Tafelsalz?",
        "option1": "Natriumchlorid",
        "option2": "Kaliumchlorid",
        "option3": "Calciumchlorid",
        "option4": "Eisenchlorid",
        "answer": 1,
    },
    {
        "id": 12,
        "question": "Welche Gasart wird oft als Lachgas bezeichnet?",
        "option1": "Methan",
        "option2": "Stickstoff",
        "option3": "Sauerstoff",
        "option4": "Distickstoffmonoxid",
        "answer": 4,
    },
    {
        "id": 13,
        "question": "Was ist der chemische Symbol für Gold?",
        "option1": "Ag",
        "option2": "Au",
        "option3": "Fe",
        "option4": "Pt",
        "answer": 2,
    },
    {
        "id": 14,
        "question": "Welches ist das größte Organ im menschlichen Körper?",
        "option1": "Leber",
        "option2": "Herz",
        "option3": "Gehirn",
        "option4": "Haut",
        "answer": 4,
    },
    {
        "id": 15,
        "question": "Welches Gas wird von Pflanzen während der Photosynthese freigesetzt?",
        "option1": "Sauerstoff",
        "option2": "Stickstoff",
        "option3": "Kohlendioxid",
        "option4": "Wasserstoff",
        "answer": 1,
    },
    {
        "id": 16,
        "question": "Welcher Planet wird als der 'Rote Planet' bezeichnet?",
        "option1": "Venus",
        "option2": "Erde",
        "option3": "Mars",
        "option4": "Jupiter",
        "answer": 3,
    },
    {
        "id": 17,
        "question": "Welches chemische Element hat das Symbol 'Na'?",
        "option1": "Natrium",
        "option2": "Nickel",
        "option3": "Neon",
        "option4": "Stickstoff",
        "answer": 1,
    },
    {
        "id": 18,
        "question": "Wie lautet die chemische Formel für Kohlendioxid?",
        "option1": "CO2",
        "option2": "H2O",
        "option3": "O2",
        "option4": "CH4",
        "answer": 1,
    },
    {
        "id": 19,
        "question": "Welche Einheit wird für die Messung der Energie verwendet?",
        "option1": "Kilogramm",
        "option2": "Meter",
        "option3": "Joule",
        "option4": "Volt",
        "answer": 3,
    },
    {
        "id": 20,
        "question": "Was ist die höchste Bergspitze der Welt?",
        "option1": "Mount Kilimanjaro",
        "option2": "Mount Everest",
        "option3": "Mount McKinley",
        "option4": "Mount Fuji",
        "answer": 2,
    },
]

for question in questions:
    cursor.execute(
        """INSERT OR IGNORE INTO questions (id, question, option1, option2, option3, option4, answer, answered)
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
