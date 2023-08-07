from flask import Flask, render_template, redirect, url_for, request, session
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, EmailField, StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, DataRequired, Email, EqualTo
import sqlite3
import random

app = Flask(__name__)

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max= 15),])
    password = PasswordField('password', validators=[InputRequired(), Length (min=8, max=80)])
    SubmitField= SubmitField('Log In')

class SignUpForm(FlaskForm):
    email=EmailField('email', validators=[InputRequired(), Length(max=50)])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

def reset_quiz():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # Markierung der beantworteten Fragen entfernen
    cursor.execute('UPDATE questions SET answered = 0')
    conn.commit()

    # Verbindung zur Datenbank schließen
    conn.close()

def initialize_score():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # Tabelle 'scores' erstellen, wenn sie nicht existiert
    cursor.execute('''CREATE TABLE IF NOT EXISTS scores (
                        id INTEGER PRIMARY KEY,
                        score INTEGER DEFAULT 0
                    )''')

    # Prüfen, ob bereits ein Eintrag in der Tabelle vorhanden ist
    cursor.execute('SELECT * FROM scores')
    existing_score = cursor.fetchone()

    if not existing_score:
        # Kein Eintrag vorhanden, wir setzen den Punktestand auf 0
        cursor.execute('INSERT INTO scores (score) VALUES (?)', (0,))
        conn.commit()

    conn.close()

#User in DB einsetzen
def insert_user(email, username, password):
        conn = sqlite3.connect('quiz.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (email, username, password) VALUES (?, ?, ?)', (email, username, password))
        conn.commit()
        conn.close()


# Score aktualisieren
def update_score():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # Punktestand aus der Datenbank abrufen
    cursor.execute('SELECT score FROM scores')
    current_score = cursor.fetchone()

    if current_score:
        # Punktestand erhöhen
        score = current_score[0] + 1

        # Punktestand in der Datenbank aktualisieren
        cursor.execute('UPDATE scores SET score = ?', (score,))
        conn.commit()

    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('logIn'))

@app.route('/signup', methods=['GET','POST'])
def signup():
        form=SignUpForm()
        if request.method == 'POST':
            email = request.form.get('email')
            username= request.form.get('username')
            password= request.form.get('password')
            insert_user(email,username,password)
            return redirect(url_for('logIn'))

        else:   
            return render_template ('signup.html', form=form)
        

@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    if request.method=='POST':
        return redirect(url_for('/quiz'))
    else:
        return render_template('homepage.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        question_id = request.form['question_id']
        user_answer = request.form['answer']

        # Frage aus der Datenbank abrufen
        cursor.execute('SELECT * FROM questions WHERE id = ?', (question_id,))
        question = cursor.fetchone()

        if question and user_answer == str(question[6]):
            message = "Richtig!"
            update_score()  # Punktestand aktualisieren
        else:
            message = "Falsch!"
    else:
        message = None

    # Punktestand aus der Datenbank abrufen
    cursor.execute('SELECT score FROM scores')
    current_score = cursor.fetchone()
    score = current_score[0] if current_score else 0

    # Alle unbeantworteten Fragen aus der Datenbank abrufen
    cursor.execute('SELECT * FROM questions WHERE answered = 0')
    questions = cursor.fetchall()

    if not questions:
        # Alle Fragen wurden beantwortet, das Quiz startet von vorne
        reset_quiz()

        # Punktestand auf 0 zurücksetzen
        cursor.execute('UPDATE scores SET score = 0')
        conn.commit()

        conn.close()

        return redirect('/homepage')  # Weiterleitung zur Homepage

        # Homepage-Seite anzeigen
        # return render_template('homepage.html')

    # Eine zufällige Frage auswählen
    question = random.choice(questions)

    # Frage als beantwortet markieren
    cursor.execute('UPDATE questions SET answered = 1 WHERE id = ?', (question[0],))
    conn.commit()

    conn.close()

    return render_template('quiz.html', question=question, message=message, score=score)

@app.route('/gkquiz', methods=['GET', 'POST'])
def gkquiz():
    print("Entered gkquiz route.")
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    
    if request.method == 'POST':
        print("Form submitted.")
        question_id = request.form['question_id']
        user_answer = request.form['answer']
        # Frage aus der Datenbank abrufen
        cursor.execute('SELECT * FROM questions WHERE id = ?', (question_id,))
        question = cursor.fetchone()
        
        if question and user_answer == str(question[6]):
            message = "Richtig!"
        else:
            message = "Falsch!"
    else:
        message = None
   
    # Alle unbeantworteten Fragen aus der Datenbank abrufen
    cursor.execute('SELECT * FROM questions WHERE answered = 0')
    questions = cursor.fetchall()
    
    if not questions:
        # Alle Fragen wurden beantwortet, das Quiz startet von vorne
        reset_quiz()

        # Punktestand auf 0 zurücksetzen
        cursor.execute('UPDATE scores SET score = 0')
        conn.commit()

        conn.close()

        return redirect('/homepage')  # Weiterleitung zur Homepage

    #Eine zufällige Frage auswählen
    question = random.choice(questions)

    #Frage als beantwortet markieren
    cursor.execute('UPDATE questions SET answered = 1 WHERE id = ?', (question[0],))
    conn.commit()

    conn.close()

    return render_template('genQuiz.html', question=question, message=message)


if __name__ == '__main__':
    initialize_score()  #Punktestand initialisieren
    app.run()
