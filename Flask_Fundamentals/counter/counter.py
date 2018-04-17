from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'MyDude'

@app.route('/')
def index():
    session['counter'] = 1
    return render_template('index.html')

@app.route('/add')
def add():
    session['counter'] += 1
    return redirect('/display')

@app.route('/addtwo')
def addtwo():
    session['counter'] += 2
    return redirect('/display')

@app.route('/reset')
def reset():
    session['counter'] = 1
    return redirect('/display')

@app.route('/display')
def display():
    return render_template('index.html')

app.run(debug=True)
