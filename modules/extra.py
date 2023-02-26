from app import app
from flask import redirect, url_for, request

@app.route('/extra', methods = ['POST'])
def extra():
    if request.method == 'POST':
        if request.form['answer'] == "Yes":
            return redirect(url_for('reentry'))
        elif request.form['answer'] == "No":
            return redirect(url_for('main'))
        else:
            pass