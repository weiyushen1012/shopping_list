from datetime import datetime
from models.init import db


class ShoppingListItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    updated = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    shopping_list_id = db.Column(db.Integer, db.ForeignKey('shopping_list.id'), nullable=False)

    name = db.Column(db.String(1024), nullable=False)
    category = db.Column(db.String(256))
    quantity = db.Column(db.Integer, default=0, nullable=False)
    finished = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<ShoppingListItem(id={self.id},created={self.created},updated={self.updated}' \
               f',shopping_list_id={self.shopping_list_id}>'
