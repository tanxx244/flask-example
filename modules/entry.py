from app import app
from flask import redirect, url_for, request, make_response
from datetime import datetime

@app.route('/entry', methods = ['POST', 'GET'])
def entry():
    if request.method == 'POST':
        name = request.form['name']
        invoice = request.form['invoice']
        procedure = request.form['procedure']
        amount = request.form['amount']
        claim = request.form['claim']
        cash = request.form['cash']
        paynow = request.form['paynow']
        nets = request.form['nets']
        insurance = request.form['insurance']
        bc = request.form['bc']
        labmat = request.form['labmat']
        total = request.form['total']
        nettotal = request.form['nettotal']

        res = make_response({"message":"Cookies set!"})
        res.set_cookie("date", datetime.today().strftime('%Y-%m-%d'))
        res.set_cookie("name", name)
        res.set_cookie("invoice", invoice)
        res.set_cookie("procedure", procedure)
        res.set_cookie("amount", amount)
        res.set_cookie("claim", claim)
        res.set_cookie("cash", cash)
        res.set_cookie("paynow", paynow)
        res.set_cookie("nets", nets)
        res.set_cookie("insurance", insurance)
        res.set_cookie("bc", bc)
        res.set_cookie("labmat", labmat)
        res.set_cookie("total", total)
        res.set_cookie("nettotal", nettotal)

        return redirect(url_for('verify'))
    else:
        name = request.args.get('name')
        invoice = request.args.get('invoice')
        procedure = request.args.get('procedure')
        amount = request.args.get('amount')
        claim = request.args.get('claim')
        cash = request.args.get('cash')
        paynow = request.args.get('paynow')
        nets = request.args.get('nets')
        insurance = request.args.get('insurance')
        bc = request.args.get('bc')
        labmat = request.args.get('labmat')
        total = request.args.get('total')
        nettotal = request.args.get('nettotal')

        res = make_response({"message":"Cookies set!"})
        res.set_cookie("date", datetime.today().strftime('%Y-%m-%d'))
        res.set_cookie("name", name)
        res.set_cookie("invoice", invoice)
        res.set_cookie("procedure", procedure)
        res.set_cookie("amount", amount)
        res.set_cookie("claim", claim)
        res.set_cookie("cash", cash)
        res.set_cookie("paynow", paynow)
        res.set_cookie("nets", nets)
        res.set_cookie("insurance", insurance)
        res.set_cookie("bc", bc)
        res.set_cookie("labmat", labmat)
        res.set_cookie("total", total)
        res.set_cookie("nettotal", nettotal)

        return redirect(url_for('verify'))