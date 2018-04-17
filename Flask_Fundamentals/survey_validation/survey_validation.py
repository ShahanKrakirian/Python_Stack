from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
app.secret_key = 'NobodyKnows'

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/result', methods=['post'])

def route():
    if len(request.form['name']) == 0 or len(request.form['comment']) == 0:
        flash('Please fill out name and comment sections.')
    elif len(request.form['name']) > 120 or len(request.form['comment']) > 120:
        flash('Okay, not so much input please...')
    else:
        name = request.form['name']
        location = request.form['location']
        language = request.form['language']
        comment = request.form['comment']
        print request.form
        return render_template('result.html', name=name, location=location, language=language, comment=comment)
    return render_template('index.html')

app.run(debug=True)