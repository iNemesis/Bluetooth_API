from datetime import datetime
from flask import *
from flask_sqlalchemy import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/Users/antho/Documents/api_example/todo.db'

db = SQLAlchemy(app)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nom = db.Column(db.String(20), nullable=False)
    prenom = db.Column(db.String(20), nullable=False)
    telephone = db.Column(db.String(20))
    rue = db.Column(db.String(80), nullable=False)
    ville = db.Column(db.String(50), nullable=False)
    code_postal = db.Column(db.String(10), nullable=False)
    pays = db.Column(db.String(40), nullable=False)
    adresse_mac = db.Column(db.String(20))
    date_naissance = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True)
    date_creation = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    visites = db.relationship('Visite', backref='client', lazy='dynamic')

class Visite(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))






@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
