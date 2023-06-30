import os
from flask import Flask, render_template, redirect, url_for, request
import random

app = Flask(__name__)

# Fragen und Antworten in einer Liste
quiz = [
    {
        "id" : 1,
        "question": "Was ist die Hauptstadt von Frankreich?",
        "options": ["Madrid", "Paris", "Berlin", "London"],
        "answer": "2"
    },
    {
        "id" : 2,
        "question": "Wie viele Planeten hat unser Sonnensystem?",
        "options": ["7", "8", "9", "10"],
        "answer": "2"
    },
    {
        "id" : 3,
        "question": "Was ist die Hauptstadt von Kanada?",
        "options": ["Ottawa", "Toronto", "Montreal", "Vancouver"],
        "answer": "1"
    }
] 

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    DATABASE=os.path.join(app.instance_path, 'todos.sqlite')
)


@app.route('/')
def index():
    return redirect(url_for('gameloop', question_id = 1)) ##logIn

@app.route('/gameloop/<int:question_id>', methods=['GET', 'POST'])
def gameloop(question_id):
    question = next((q for q in quiz if q["id"] == question_id), None)
    if question:
        if request.method == 'POST' and 'answer' in request.form:
            user_answer = request.form['answer']
            correct_answer = question["answer"]
            if str(user_answer) == str(correct_answer):
                return redirect(url_for('gameloop', question_id=question_id + 1))
            else:
                return redirect(url_for('gameloop', question_id=question_id))
        else:
            return render_template('gameloop.html', question=question, question_index=question_id)
    else:
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
  
@app.route ('/homepage', methods=['GET','POST'])
def homepage():
    if request.method == 'POST':
        return redirect(url_for('gameloop', question_id=1))
    else:
        return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=True)


