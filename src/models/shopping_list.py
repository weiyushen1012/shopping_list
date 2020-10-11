from datetime import datetime
from models.init import db


class ShoppingList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    updated = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<ShoppingList(id={self.id},created={self.created},updated={self.updated},user_id={self.user_id}>'
