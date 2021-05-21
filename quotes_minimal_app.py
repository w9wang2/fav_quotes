# import Flask class
from flask import Flask

# to instantiate a Flask class - to create an instance of the Flask class
app = Flask(__name__)

# to use a root decorator to create a root for the app
# i.e., to tell the app what URL to use to trigger the function right below the decorator
@app.route('/') # '/' is the root page
def index():
    return '<h1> Hello World <h1>'

@app.route('/about')
def about():
    return '<h1> Hello World fron about page <h1>'

@app.route('/quotes')
def quotes():
    return '<h1> Life is a journey <h1>'