import random
import sqlite3

from flask import Flask, redirect, render_template, request, session, url_for
from flask_wtf import FlaskForm
from wtforms.fields import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired, Length

from db import insert_user, reset_quiz, save_score

app = Flask(__name__)
app.secret_key = "34"
current_score = 0


class LoginForm(FlaskForm):
    # Felder für die Anmeldung
    username = StringField(
        "username",
        validators=[
            InputRequired(),
            Length(min=4, max=15),
        ],
    )
    password = PasswordField(
        "password", validators=[InputRequired(), Length(min=8, max=80)]
    )
    SubmitField = SubmitField("Log In")


class SignUpForm(FlaskForm):
    # Felder für die Registrierung
    email = EmailField("email", validators=[InputRequired(), Length(max=50)])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")


# Indexroute, leitet auf den Login um
@app.route("/", methods=["GET", "POST"])
def index():
    return redirect(url_for("logIn"))


# Loginroute
@app.route("/logIn", methods=["GET", "POST"])
def logIn():
    form = LoginForm()
    if (
        request.method == "POST"
    ):  # wird ausgeführt wenn man auf den log in button drückt
        username = request.form.get("username")
        password = request.form.get("password")
        # daten aus der Datenbank holen
        conn = sqlite3.connect("quiz.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username= ? AND password= ?",
            (username, password),
        )
        user = cursor.fetchone()
        conn.close()

        if user:
            session["user_id"] = user[0]  # user id in session speichern
            session.permanent = True
            return redirect(url_for("homepage"))
        else:
            return redirect(url_for("logIn"))
    else:
        return render_template("login-page.html", form=form)


# Registerroute
@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        insert_user(email, username, password)
        return redirect(url_for("logIn"))

    else:
        return render_template("signup.html", form=form)


# Startseite für den Benutzer
@app.route("/homepage", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        return redirect(url_for("/quiz"))
    else:
        return render_template("homepage.html")


# Rush Quizroute
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    global current_score
    if request.method == "POST":
        if "question_id" in request.form and "answer" in request.form:
            question_id = request.form["question_id"]
            user_answer = request.form["answer"]

            # Frage aus der Datenbank abrufen
            cursor.execute("SELECT * FROM questions WHERE id = ?", (question_id,))
            question = cursor.fetchone()

            if question and user_answer == str(question[6]):
                message = "Richtig!"
                current_score = current_score + 1
            else:
                message = "Falsch!"
        else:  # neu
            reset_quiz()  # quiz startet wieder von vorne
            save_score(session["user_id"], current_score)
            current_score = 0
            conn.close()
            return redirect("/highscores")
    else:
        message = None

    # alle unbeantworteten Fragen aus der Datenbank abrufen
    cursor.execute("SELECT * FROM questions WHERE answered = 0")
    questions = cursor.fetchall()

    if not questions:
        # Alle Fragen wurden beantwortet, das Quiz startet von vorne
        reset_quiz()

        save_score(session["user_id"], current_score)  # Punktestand speichern

        current_score = 0

        return redirect("/highscores")  # Weiterleitung zur highscore seite

    # Eine zufällige Frage auswählen
    question = random.choice(questions)

    # Frage als beantwortet markieren
    cursor.execute("UPDATE questions SET answered = 1 WHERE id = ?", (question[0],))
    conn.commit()

    conn.close()

    return render_template(
        "quiz.html", question=question, message=message, score=current_score
    )


# Quizroute für allgemeines Wissen
@app.route("/gkquiz", methods=["GET", "POST"])
def gkquiz():
    print("Entered gkquiz route.")
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    if request.method == "POST":
        print("Form submitted.")
        question_id = request.form["question_id"]
        user_answer = request.form["answer"]
        # Frage aus der Datenbank abrufen
        cursor.execute("SELECT * FROM questions WHERE id = ?", (question_id,))
        question = cursor.fetchone()

        if question and user_answer == str(question[6]):
            message = "Richtig!"
        else:
            message = "Falsch!"
    else:
        message = None

    # Alle unbeantworteten Fragen aus der Datenbank abrufen
    cursor.execute("SELECT * FROM questions WHERE answered = 0")
    questions = cursor.fetchall()

    if not questions:
        # Alle Fragen wurden beantwortet, das Quiz startet von vorne
        reset_quiz()

        # Punktestand auf 0 zurücksetzen
        cursor.execute("UPDATE scores SET score = 0")
        conn.commit()

        conn.close()

        return redirect("/homepage")

    # Eine zufällige Frage auswählen, falls es unbeantwortete Fragen gibt
    question = random.choice(questions)

    # Frage als beantwortet markieren
    cursor.execute("UPDATE questions SET answered = 1 WHERE id = ?", (question[0],))
    conn.commit()

    conn.close()

    return render_template("gkQuiz.html", question=question, message=message)


# Anzeigen der höchsten Punktzahl
@app.route("/highscores", methods=["GET"])
def highscores():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    # Höchste Punktestände für jeden Benutzer abrufen
    cursor.execute(
        "SELECT username, MAX(score) FROM users JOIN scores ON users.id = scores.user_id GROUP BY users.id"
    )
    high_scores = cursor.fetchall()

    conn.close()

    return render_template("highscores.html", high_scores=high_scores)


if __name__ == "__main__":
    app.run()
