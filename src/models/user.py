from datetime import datetime
from models.init import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)
    shopping_lists = db.relationship('ShoppingList', backref='user', lazy=True)

    def __repr__(self):
        return f'<User(id={self.id},email={self.email},created={self.created},updated={self.updated}>'
