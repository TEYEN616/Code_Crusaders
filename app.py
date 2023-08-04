from flask import Flask, render_template, request, redirect
import sqlite3
import random

app = Flask(__name__)

def reset_quiz():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE questions SET answered = 0')
    conn.commit()

    conn.close()

def initialize_score():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS scores (
                        id INTEGER PRIMARY KEY,
                        score INTEGER DEFAULT 0
                    )''')

    cursor.execute('SELECT * FROM scores')
    existing_score = cursor.fetchone()

    if not existing_score:
        cursor.execute('INSERT INTO scores (score) VALUES (?)', (0,))
        conn.commit()

    conn.close()

def update_score():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    cursor.execute('SELECT score FROM scores')
    current_score = cursor.fetchone()

    if current_score:
        score = current_score[0] + 1

        cursor.execute('UPDATE scores SET score = ?', (score,))
        conn.commit()

    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect('/quiz') 
    
    return render_template('homepage.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        question_id = request.form['question_id']
        user_answer = request.form['answer']

        cursor.execute('SELECT * FROM questions WHERE id = ?', (question_id,))
        question = cursor.fetchone()

        if question and user_answer == str(question[6]):
            message = "Richtig!"
            update_score()  
        else:
            message = "Falsch!"
    else:
        message = None

    cursor.execute('SELECT score FROM scores')
    current_score = cursor.fetchone()
    score = current_score[0] if current_score else 0

    cursor.execute('SELECT * FROM questions WHERE answered = 0')
    questions = cursor.fetchall()

    if not questions:
        reset_quiz()

        cursor.execute('UPDATE scores SET score = 0')
        conn.commit()

        conn.close()

        return redirect('/homepage') 

    question = random.choice(questions)

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

        cursor.execute('SELECT * FROM questions WHERE id = ?', (question_id,))
        question = cursor.fetchone()
        
        if question and user_answer == str(question[6]):
            message = "Richtig!"
        else:
            message = "Falsch!"
    else:
        message = None
   
    cursor.execute('SELECT * FROM questions WHERE answered = 0')
    questions = cursor.fetchall()
    
    if not questions:
        reset_quiz()

        cursor.execute('UPDATE scores SET score = 0')
        conn.commit()

        conn.close()

        return redirect('/homepage')  

    question = random.choice(questions)

    cursor.execute('UPDATE questions SET answered = 1 WHERE id = ?', (question[0],))
    conn.commit()

    conn.close()

    return render_template('genQuiz.html', question=question, message=message)


if __name__ == '__main__':
    initialize_score()
    app.run()
