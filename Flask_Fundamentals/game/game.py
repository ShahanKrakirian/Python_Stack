from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/left1')
def left1():
    return render_template('left1.html')

@app.route('/right1')
def right1():
    return render_template('right1.html')

@app.route('/left2')
def left2():
    return render_template('left2.html')

@app.route('/right2')
def right2():
    return render_template('right2.html')

@app.route('/left3')
def left3():
    return render_template('left3.html')

@app.route('/right3')
def right3():
    return render_template('right3.html')


app.run(debug=True)