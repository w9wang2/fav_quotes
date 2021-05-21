from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# connect local PostgreSQL database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:iamhere@123@localhost/quotes'

# connect cloud Heroku database
# due the new changes of SQLAlchemy, the name in Heroku "postgres" need to be changed to "postgresql"git
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://htiackhtuehkqk:7f6c8dd64a216e3d8c6f1103cc3480d6b60803b7090b5425da63ff184f46009c@ec2-18-214-140-149.compute-1.amazonaws.com:5432/dcm7lvtptdklts'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://htiackhtuehkqk:7f6c8dd64a216e3d8c6f1103cc3480d6b60803b7090b5425da63ff184f46009c@ec2-18-214-140-149.compute-1.amazonaws.com:5432/dcm7lvtptdklts'

# do not track Alchemy modefications due to taking large memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # do not track

# cretae an instance of SQLAlchemy
db = SQLAlchemy(app)

#create a table class Favquotes with three columns (variables)
class Favquotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))


@app.route('/')
def index():
    result = Favquotes.query.all()
    #return '<h1> Hello World <h1>'
    return render_template('index.html', result = result)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author, quote=quote)
    db.session.add(quotedata) # add the quotedata to database table
    db.session.commit()

    #return redirect(url_for('index.html'))
    return redirect(url_for('index')) #return to index view function, not the index.html page