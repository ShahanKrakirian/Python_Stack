from flask import Flask, redirect, request, render_template, session
import random
app = Flask(__name__)
app.secret_key = 'NobodyKnows'

@app.route('/')
def index():
    #If we don't have a winning number, generate one.
    if not 'number' in session:
        session['number'] = random.randrange(1,101)
    print "Winning Number:", session['number']
    #Set initial value for "status". 
    session['status'] = 'none'
    #If we have a user guess, set status accordingly. If not, do nothing.
    if 'user_guess' in session:
        if int(session['user_guess']) == int(session['number']):
            session['status'] = 'correct'
            return redirect('/reset')
        elif int(session['user_guess']) > int(session['number']):
            session['status'] = 'high'
        elif int(session['user_guess']) < int(session['number']):
            session['status'] = "low"
    session['user_guess'] = 0
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['user_guess'] = request.form['guess']
    return redirect('/')

@app.route('/correct')
def correct():
    return render_template('correct.html')

@app.route('/reset')
def reset():
    session.pop('status')
    session.pop('user_guess')
    session.pop('number')
    return render_template('correct.html')

app.run(debug=True)