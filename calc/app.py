from operations import add, sub, mult, div

from flask import Flask, request

app = Flask(__name__)

@app.route("/add")
'''Add a and b'''
def addition():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a,b)

    return str(result)

@app.route("/sub")
'''Subtract a and b'''
def subtract():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a,b)
    return str(result)

@app.route("/mult")
'''Multiply a and b'''
def mulyiply():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b)
    return str(result)

@app.route("/div")
'''Divide a and b'''
def divide():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)
    return str(result)