from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    tmnt = "/static/ninjas/tmnt.png"
    return render_template('ninja.html', name=tmnt)

@app.route('/ninja/<colorname>')
def colorname(colorname):
    if colorname == 'blue' or colorname == 'orange' or colorname == 'red' or colorname == 'purple':
        return render_template('ninja.html', name="/static/ninjas/"+colorname+".jpg")
    else:
        return render_template('ninja.html', name="/static/ninjas/notapril.jpg")

app.run(debug=True)