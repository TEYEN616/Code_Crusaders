import operator
import sqlite3

from flask import Flask, redirect, render_template, request, session, url_for
from flask_wtf import FlaskForm
from wtforms.fields import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length

from db import (
    checkUser,
    getHighscores,
    getNextQuestion,
    getQuestion,
    getUnansweredQuestions,
    insert_user,
    reset_quiz,
    save_score,
)

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
        user = checkUser(username, password)
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
            question = getQuestion(question_id)

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
    questions = getUnansweredQuestions()

    if not questions:
        # Alle Fragen wurden beantwortet, das Quiz startet von vorne
        reset_quiz()

        save_score(session["user_id"], current_score)  # Punktestand speichern

        current_score = 0

        return redirect("/highscores")  # Weiterleitung zur highscore seite

    question = getNextQuestion(questions)

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

        question = getQuestion(question_id)

        if question and user_answer == str(question[6]):
            message = "Richtig!"
        else:
            message = "Falsch!"
    else:
        message = None

    questions = getUnansweredQuestions()

    if not questions:
        # Alle Fragen wurden beantwortet, das Quiz startet von vorne
        reset_quiz()

        return redirect("/homepage")

    question = getNextQuestion(questions)

    return render_template("gkQuiz.html", question=question, message=message)


# Anzeigen der höchsten Punktzahl
@app.route("/highscores", methods=["GET"])
def highscores():
    # highscores aus der db holen
    high_scores = getHighscores()
    # score speichern in absteigender Reihenfolge
    high_scores.sort(key=operator.itemgetter(1), reverse=True)

    return render_template("highscores.html", high_scores=high_scores)


if __name__ == "__main__":
    app.run()
