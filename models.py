from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class System(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    device = db.Column(db.String(255))
    user = db.relationship("User", backref='system')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    system_id = db.Column(db.Integer, db.ForeignKey('system.id'))



