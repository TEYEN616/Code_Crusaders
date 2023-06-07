import os
from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    DATABASE=os.path.join(app.instance_path, 'todos.sqlite')
)


@app.route('/')
def index():
    return redirect(url_for('logIn'))


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


