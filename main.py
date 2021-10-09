from flask import Flask, render_template, request
from tinydb import TinyDB

db = TinyDB('db.json')

app = Flask(__name__)

# Formularz

def formularz(form) -> bool:
    if '' in form.values():
        return False

    db.insert(form)
    return True

# Routing

@app.route('/')
def route_home():
    return render_template('formularz.html')

@app.route('/formularz')
def route_formularz():
    if formularz(dict(request.args)):
        return "OK"
    return "Błąd"

if __name__ == '__main__':
    app.run()
