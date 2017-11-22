from datetime import datetime
from flask import *
from flask_sqlalchemy import *

"""
Configuration
"""

app = Flask(__name__)

app.config['SECRET_KEY'] = '17161a92-9c2c-4795-93ab-b3a860391d50'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@server/db'

db = SQLAlchemy(app)

"""
Tables
"""

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
    promotions = db.relationship('Promotion', secondary='promotions',
                                 backref=db.backref('clients', lazy=True),
                                 lazy='subquery')

promotions = db.Table('promotions',
    db.Column('client_id', db.Integer, db.ForeignKey('client.id'), primary_key=True),
    db.Column('promotion_id', db.Integer, db.ForeignKey('promotion.id'), primary_key=True)
)

class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)

    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))

class Visite(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Categorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30), nullable=False)

    promotions = db.relationship('Promotion', backref='categorie', lazy='dynamic')

class Detection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    adresse_mac = db.Column(db.String(20), nullable=False)

"""
API Client
"""

@app.route('/client', methods=['POST'])
def create_client():
    return ''

@app.route('/client', methods=['GET'])
def view_clients():
    return ''

@app.route('/client/<id>', methods=['PUT'])
def edit_client(id):
    return ''

@app.route('/client/<id>', methods=['DELETE'])
def delete_client(id):
    return ''

@app.route('/client/<id>', methods=['GET'])
def view_client(id):
    return ''

"""
API Visite
"""

@app.route('/visite', methods=['POST'])
def create_visite():
    return ''

@app.route('/visite', methods=['GET'])
def view_visites():
    return ''

"""
API Promotion
"""

@app.route('/promotion', methods=['POST'])
def create_promotion():
    return ''

@app.route('/promotion', methods=['GET'])
def view_promotions():
    return ''

@app.route('/promotion/<id>', methods=['PUT'])
def edit_promotion(id):
    return ''

@app.route('/promotion/<id>', methods=['DELETE'])
def delete_promotion(id):
    return ''

@app.route('/promotion/<id>', methods=['GET'])
def view_promotion(id):
    return ''

"""
API Categorie
"""

@app.route('/categorie', methods=['POST'])
def create_categorie():
    return ''

@app.route('/categorie', methods=['GET'])
def view_categories():
    return ''

"""
Run
"""

if __name__ == '__main__':
    app.run(debug=True)