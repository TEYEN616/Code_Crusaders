import os

from flask import Flask, render_template, redirect, url_for, request, session
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import InputRequired, Length

app = Flask(__name__)

# Fragen und Antworten in einer Liste
quiz = [
    
    {
        "id": 1,
        "question": "Wie heißt die größte Wüste der Welt?",
        "options": ["Gobi-Wüste", "Atacama-Wüste", "Sahara-Wüste", "Taklamakan-Wüste"],
        "answer": "3"
    },
    {
        "id": 2,
        "question": "Welches ist das längste Flussystem der Welt?",
        "options": ["Nil", "Mississippi", "Amazonas", "Jangtse"],
        "answer": "3"
    },
    {
        "id": 3,
        "question": "Welche Farbe hat die Schale einer Zitrone?",
        "options": ["Grün", "Gelb", "Orange", "Weiß"],
        "answer": "2"
    },
    {
        "id": 4,
        "question": "Welche ist die größte Insel der Welt?",
        "options": ["Grönland", "Neuguinea", "Borneo", "Madagaskar"],
        "answer": "1"
    },
    {
        "id": 5,
        "question": "Welcher Planet ist der vierte in unserem Sonnensystem?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": "1"
    },
    {
        "id": 6,
        "question": "Wie viele Elemente enthält das Periodensystem?",
        "options": ["98", "105", "118", "124"],
        "answer": "3"
    },
    {
        "id": 7,
        "question": "Welches Land hat die längste Küstenlinie der Welt?",
        "options": ["Russland", "Kanada", "Australien", "Brasilien"],
        "answer": "2"
    },
    {
        "id": 8,
        "question": "Wie viele Kontinente gibt es auf der Erde?",
        "options": ["5", "6", "7", "8"],
        "answer": "3"
    },
    {
        "id": 9,
        "question": "Wer hat die Relativitätstheorie entwickelt?",
        "options": ["Isaac Newton", "Albert Einstein", "Max Planck", "Nikola Tesla"],
        "answer": "2"
    },
    {
        "id": 10,
        "question": "Wie viele Milliliter sind in einem Liter?",
        "options": ["100", "500", "1000", "1500"],
        "answer": "3"
    },
    {
        "id" : 11,
        "question": "Was ist die Hauptstadt von Frankreich?",
        "options": ["Madrid", "Paris", "Berlin", "London"],
        "answer": "2"
    },
    {
        "id" : 12,
        "question": "Wie viele Planeten hat unser Sonnensystem?",
        "options": ["7", "8", "9", "10"],
        "answer": "2"
    },
    {
        "id" : 13,
        "question": "Was ist die Hauptstadt von Kanada?",
        "options": ["Ottawa", "Toronto", "Montreal", "Vancouver"],
        "answer": "1"
    }
] 

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    DATABASE=os.path.join(app.instance_path, 'todos.sqlite')
)
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max= 15),])
    password = PasswordField('password', validators=[InputRequired(), Length (min=8, max=80)])
    SubmitField= SubmitField('Log In')


class SignUpForm(FlaskForm):
    email=EmailField('email', validators=[InputRequired(), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max= 15),])
    password = PasswordField('password', validators=[InputRequired(), Length (min=8, max=80)])

@app.route('/', methods=['GET', 'POST'])
def index():
        return redirect(url_for('logIn'))


@app.route('/gameloop/<int:question_id>', methods=['GET', 'POST'])
def gameloop(question_id):
    question = next((q for q in quiz if q["id"] == question_id), None)
    
    if question:
        if request.method == 'POST' and 'answer' in request.form:
            user_answer = request.form['answer']
            correct_answer = question["answer"]
            
            if str(user_answer) == str(correct_answer):
                message = "Richtig!"
                next_question_id = question_id + 1
                next_question = next((q for q in quiz if q["id"] == next_question_id), None)
                if next_question:
                    return render_template('gameloop.html', question=next_question, question_index=next_question_id, message=message)
                else:
                    return redirect(url_for('index'))
            else:
                message = "Falsch!"
                return render_template('gameloop.html', question=question, question_index=question_id, message=message)
        else:
            message = ""
            return render_template('gameloop.html', question=question, question_index=question_id, message=message)
    else:
        return redirect(url_for('index'))

    
@app.route('/signup', methods=['GET','POST'])
def signup():
        form=SignUpForm()
        if request.method == 'POST':
            email = request.form.get('email')
            username= request.form.get('username')
            password= request.form.get('password')
            password= request.form.get('confirm_password')

            return redirect(url_for('index'))
        else:
            return render_template ('signup.html', form=form)

@app.route ('/logIn', methods=['GET','POST'])
def logIn(): 
    form=LoginForm()
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')

        return redirect(url_for('homepage'))
        ##session['logged_in'] = True
        
    else:
        return render_template('login-page.html',form=form) 
  
@app.route ('/homepage', methods=['GET','POST'])
def homepage():
    if request.method == 'POST':
        return redirect(url_for('gameloop', question_id=1))
    else:
        return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=True)

##Punkte zähler
##Richtig und falsch message 
##mehr fragen

