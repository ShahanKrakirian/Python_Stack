from flask import Flask, redirect, render_template, session, request
import random
app = Flask(__name__)
app.secret_key = 'NobodyKnows'

@app.route('/')
def index(): 
    if not 'total' in session and not 'phrase' in session:
        session['total'] = 0
        session['phrase'] = []
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calc():

    if request.form['location'] == 'farm':
        addme = random.randrange(10,21)
        session['phrase'].insert(0, "You harvested " + str(addme) + " gold!")
        session['total'] += addme
    if request.form['location'] == 'cave':
        addme = random.randrange(5,11)
        session['phrase'].insert(0, "You dug up " + str(addme) + " gold!")
        session['total'] += addme
    if request.form['location'] == 'house':
        addme = random.randrange(2,6)
        session['phrase'].insert(0, "You asked your grandmother for " + str(addme) + " gold! She gave it to you!")
        session['total'] += addme
    if request.form['location'] == 'casino':
        addme = random.randrange(-50,51)
        if addme >= 0:
            session['phrase'].insert(0, "You got lucky this time. " + str(addme) + " gold.")
        else: session['phrase'].insert(0, str(addme) + " gold. Maybe you can win it back...")
        session['total'] += addme
        
    return redirect('/')

app.run(debug=True)