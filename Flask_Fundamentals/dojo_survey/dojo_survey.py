from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/result', methods=['post'])

def route():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    print request.form
    return render_template('result.html', name=name, location=location, language=language, comment=comment)


app.run(debug=True)