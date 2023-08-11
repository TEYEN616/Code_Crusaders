import random
import sqlite3

from flask import Flask, redirect, render_template, request, session, url_for
from flask_wtf import FlaskForm
from wtforms.fields import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired, Length

from db import initialize_score, insert_user, reset_quiz, update_score

app = Flask(__name__)
app.secret_key = "34"


class LoginForm(FlaskForm):
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
    email = EmailField("email", validators=[InputRequired(), Length(max=50)])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")


@app.route("/", methods=["GET", "POST"])
def index():
    return redirect(url_for("logIn"))


## if request.method == "POST":
##     return redirect("/quiz")

##return render_template("homepage.html")


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


@app.route("/homepage", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        return redirect(url_for("/quiz"))
    else:
        return render_template("homepage.html")

    # return render_template("homepage.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    if request.method == "POST":
        question_id = request.form["question_id"]
        user_answer = request.form["answer"]

        # Frage aus der Datenbank abrufen
        cursor.execute("SELECT * FROM questions WHERE id = ?", (question_id,))
        question = cursor.fetchone()

        if question and user_answer == str(question[6]):
            message = "Richtig!"
            update_score()  # Punktestand aktualisieren
        else:
            message = "Falsch!"
    else:
        message = None

    # Punktestand aus der Datenbank abrufen
    cursor.execute("SELECT score FROM scores")
    current_score = cursor.fetchone()
    score = current_score[0] if current_score else 0

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

        return redirect("/homepage")  # Weiterleitung zur Homepage

    # Eine zufällige Frage auswählen
    question = random.choice(questions)

    # Frage als beantwortet markieren
    cursor.execute("UPDATE questions SET answered = 1 WHERE id = ?", (question[0],))
    conn.commit()

    conn.close()

    return render_template(
        "rushquiz.html", question=question, message=message, score=score
    )


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

        return redirect("/homepage")  # Weiterleitung zur Homepage

    # Eine zufällige Frage auswählen
    question = random.choice(questions)

    # Frage als beantwortet markieren
    cursor.execute("UPDATE questions SET answered = 1 WHERE id = ?", (question[0],))
    conn.commit()

    conn.close()

    return render_template("gkQuiz.html", question=question, message=message)


if __name__ == "__main__":
    initialize_score()  # Punktestand initialisieren
    app.run()
