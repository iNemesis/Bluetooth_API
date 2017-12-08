from datetime import datetime
from flask import *
from flask_sqlalchemy import *

"""
Configuration
"""

app = Flask(__name__)

app.config['SECRET_KEY'] = '17161a92-9c2c-4795-93ab-b3a860391d50'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/db'

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

    def __init__(self, nom, prenom, telephone, rue, ville, code_postal, pays, adresse_mac, date_naissance, email, date_creation=None):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.rue = rue
        self.ville = ville
        self.code_postal = code_postal
        self.pays = pays
        self.adresse_mac = adresse_mac
        self.date_naissance = date_naissance
        self.email = email
        if date_creation != None:
            self.date_creation = date_creation


promotions = db.Table('promotions',
    db.Column('client_id', db.Integer, db.ForeignKey('client.id'), primary_key=True),
    db.Column('promotion_id', db.Integer, db.ForeignKey('promotion.id'), primary_key=True)
)

class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)

    categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))

    def __init__(self, message, categorie_id, client_id):
        self.message = message
        self.categorie_id = categorie_id
        self.client_id = client_id

class Visite(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))

    def __init__(self, client_id):
        self.client_id = client_id

class Categorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30), nullable=False)

    promotions = db.relationship('Promotion', backref='categorie', lazy='dynamic')

    def __init__(self, nom):
        self.nom = nom

class Detection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    adresse_mac = db.Column(db.String(20), nullable=False)

    def __init__(self, adresse_mac):
        self.adresse_mac = adresse_mac

"""
API Client
"""

@app.route('/client', methods=['POST'])
def create_client():
    data = request.get_json()

    new_client = Client(data['nom'], data['prenom'], data['telephone'], data['rue'], data['ville'], data['code_postal'],
                        data['pays'], data['adresse_mac'], data['date_naissance'], data['email'])
    db.session.add(new_client)
    db.session.commit()

    return jsonify({'message': 'New user created!'})

@app.route('/client', methods=['GET'])
def view_clients():
    clients = Client.query.all()
    output = []

    for client in clients:
        client_data = {}
        client_data['id'] = client.id
        client_data['nom'] = client.nom
        client_data['prenom'] = client.prenom
        client_data['telephone'] = client.telephone
        client_data['rue'] = client.rue
        client_data['ville'] = client.ville
        client_data['code_postal'] = client.code_postal
        client_data['pays'] = client.pays
        client_data['adresse_mac'] = client.adresse_mac
        client_data['date_naissance'] = client.date_naissance
        client_data['email'] = client.email
        client_data['date_creation'] = client.date_creation
        output.append(client_data)

    return jsonify({'clients' : output})

@app.route('/client/<id>', methods=['DELETE'])
def delete_client(id):
    return ''

@app.route('/client/<id>', methods=['GET'])
def view_client(id):
    client = Client.query.filter_by(id=id).first()

    if not client:
        return jsonify({'message': 'No user found!'})

    client_data = {}
    client_data['id'] = client.id
    client_data['nom'] = client.nom
    client_data['prenom'] = client.prenom
    client_data['telephone'] = client.telephone
    client_data['rue'] = client.rue
    client_data['ville'] = client.ville
    client_data['code_postal'] = client.code_postal
    client_data['pays'] = client.pays
    client_data['adresse_mac'] = client.adresse_mac
    client_data['date_naissance'] = client.date_naissance
    client_data['email'] = client.email
    client_data['date_creation'] = client.date_creation

    return jsonify({'client': client_data})

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
    try:
        db.create_all()
    except:
        print("Database non creee")
    app.run(debug=True)
