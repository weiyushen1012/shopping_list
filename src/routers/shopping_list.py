from flask import Blueprint, jsonify
from models.init import db

from configs.token_config import check_for_token
from models.shopping_list import ShoppingList

shopping_lists_api = Blueprint('list', __name__)


def serialize_list(shopping_list):
    return {
        'id': shopping_list.id,
        'created': shopping_list.created,
        'updated': shopping_list.updated,
        'user_id': shopping_list.user_id
    }


@shopping_lists_api.route('/add_shopping_list/<user_id>', methods=['POST'])
@check_for_token
def add_shopping_list(user_id):
    new_shopping_list = ShoppingList(user_id=user_id)
    db.session.add(new_shopping_list)
    db.session.commit()
    return {'message': 'shopping list created', 'shopping_list': serialize_list(new_shopping_list)}, 200


@shopping_lists_api.route('/get_shopping_lists/<user_id>', methods=['GET'])
@check_for_token
def get_shopping_lists(user_id):
    shopping_lists = ShoppingList.query.filter_by(user_id=user_id)
    return jsonify(list(map(serialize_list, shopping_lists))), 200
