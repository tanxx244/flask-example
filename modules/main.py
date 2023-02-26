from app import app
from flask import redirect, url_for, request, make_response

@app.route('/main', methods = ['POST'])
def main():
    res = make_response({"message":"Cookies deleted!"})
    res.delete_cookie("date")
    res.delete_cookie("name")
    res.delete_cookie("invoice")
    res.delete_cookie("procedure")
    res.delete_cookie("amount")
    res.delete_cookie("claim")
    res.delete_cookie("cash")
    res.delete_cookie("paynow")
    res.delete_cookie("nets")
    res.delete_cookie("insurance")
    res.delete_cookie("bc")
    res.delete_cookie("labmat")
    res.delete_cookie("total")
    res.delete_cookie("nettotal")
    
    if request.method == 'POST':
        return redirect(url_for('entry'))