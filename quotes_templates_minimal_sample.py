from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    fruits = ["apple","grapes","berries","oranges"]
    #return '<h1> Hello World <h1>'
    return render_template('index_template_minimal_sample.html', quote="Kindness needs no translation", fruits=fruits)


"""
@app.route('/about')
def about():
    return '<h1> Hello World fron about page <h1>'
    #return render_template('about.html')

@app.route('/quotes')
def quotes():
    return '<h1> Life is a journey <h1>'
    #return render_template('quotes.html')
"""