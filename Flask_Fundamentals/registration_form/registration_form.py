from flask import Flask, render_template, request, session, flash, redirect
import re
app = Flask(__name__)
app.secret_key = "NobodyKnows"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')

def index():
    return render_template('index.html')

@app.route('/result', methods=['post'])

def route():
    #Check if there are any empty inputs.
    for key in request.form:
        if request.form[key] == '':
            flash('Please fill out each section.')
            return render_template('index.html')
    #Check if passwords match and are minimum 9 characters.
    if len(request.form['password']) <= 8 or len(request.form['confirm_password']) <= 8 or request.form['password'] != request.form['confirm_password']:
        flash("Make sure your passwords match and are at least 9 characters long.")
        return render_template('index.html')
    #Check if any numbers in first or last name.
    elif request.form['first_name'].isalpha() == False or request.form['last_name'].isalpha() == False:
        flash("No numbers in your first or last name please.")
        return render_template('index.html')
    #Check if email is valid.
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email address.")
        return render_template('index.html')
    #Else success.
    else:
        flash("Thank you!")
        return redirect('/success')

@app.route('/success')

def success():
    return render_template('results.html')

app.run(debug=True)