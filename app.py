import os
from flask import Flask, render_template, redirect, url_for, request
import random

app = Flask(__name__)

# Fragen und Antworten in einer Liste
quiz = [
    {
        "question": "Was ist die Hauptstadt von Frankreich?",
        "options": ["Madrid", "Paris", "Berlin", "London"],
        "answer": "Paris"
    },
    {
        "question": "Wie viele Planeten hat unser Sonnensystem?",
        "options": ["7", "8", "9", "10"],
        "answer": "8"
    },
    {
        "question": "Was ist die Hauptstadt von Kanada?",
        "options": ["Ottawa", "Toronto", "Montreal", "Vancouver"],
        "answer": "Ottawa"
    }
] 

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    DATABASE=os.path.join(app.instance_path, 'todos.sqlite')
)


@app.route('/')
def index():
    return redirect(url_for('logIn'))

@app.route('/gameloop', methods=['Get', 'POST'])
def quiz_app():
    if request.method == 'POST':
        user_answer = request.form['answer']
        question_index = int(request.form.get('question_index', 0))
        question = quiz[question_index]
        if user_answer == "":
            return render_template('gameloop.html', question=question, message="Zeit abgelaufen! Die Frage wurde übersprungen.")
        elif question["options"][int(user_answer) - 1] == question["answer"]:
            return render_template('gameloop.html', question=question, message="Richtig!", score=1)
        else:
            return render_template('gameloop.html', question=question, message=f"Falsch! Die richtige Antwort ist {question['answer']}.")
    else:
        random.shuffle(quiz)
        return render_template('gameloop.html', question=quiz[0])


@app.route('/check_answer', methods=['POST'])
def check_answer():
    answer = request.form['answer']
    # Perform answer validation here
    # ...

    return redirect(url_for('index'))    
    
@app.route('/signup', methods=['GET','POST'])
def signup():
        if request.method == 'POST':
            email = request.form.get('email')
            username= request.form.get('username')
            password= request.form.get('password')
            password= request.form.get('confirm_password')

            # hier können wir die daten die hier gerade erfasst wurden verarbeiten. In der DB z.B. 

            return redirect(url_for('index'))
        
        return render_template ('signup.html')

@app.route ('/logIn', methods=['GET','POST'])
def logIn(): 
        if request.method == 'POST':
            username= request.form.get('username')
            password= request.form.get('password') 
            
            return redirect(url_for('signup'))

        return render_template('login-page.html')   
  
if __name__ == '__main__':
    app.run(debug=True)


