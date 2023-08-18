# Contents of this repository

This repository contains the ressources about our  web-based Quiz application:

+ Complete code for errorless interaction
+ Documentation page about the whole project

## Steps to execute the code

**Step 1:** Set up and activate a python virtual environment.

**Step 2:** Install the required Python packages from the terminal with the command `pip install -r requirements.txt` .

**Step 3:** Eine Datenbank wird mitgeliefert, möchten man jedoch diese extra anlegen muss man lediglich die alte Datenbank löschen und die fragen.py starten. 

**Step 4:** Start the webserver via `flask run --reload` .

```shell
(venv) PS C:\Users\me\projects\webapp> flask run --reload
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
```
**Step 5:** Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to sign up and start the quiz experience.

**Step 6:** Durch die Knöpfe und Eingabefelder kann man durch App steuern. 