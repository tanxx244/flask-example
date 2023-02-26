from app import app
from flask import redirect, url_for, request

@app.route('/verify', methods = ['POST'])
def verify():
    if request.method == 'POST':
        if request.form['answer'] == "Yes":
            return redirect(url_for('extra'))
        elif request.form['answer'] == "No":
            return redirect(url_for('main'))
        else:
            pass