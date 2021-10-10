from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB

db = TinyDB('db.json')

app = Flask(__name__)

# Formularz


def formularz(form: dict) -> bool:
    if '' in form.values():
        return False

    db.insert(form)
    return True

# Routing


@app.route('/')
def _home():
    return render_template('formularz.html')


@app.route('/formularz', methods=['POST', 'GET'])
def _formularz():
    if request.method == 'GET':
        return redirect(url_for('_home'))

    if request.method == 'POST':
        if formularz(dict(request.form)):
            return "OK"
        return "Błąd"


if __name__ == '__main__':
    app.run()
