import json

from flask import Blueprint, jsonify, request
from models.init import db

from configs.token_config import check_for_token
from models.shopping_list import ShoppingList
from models.shopping_list_item import ShoppingListItem

shopping_lists_api = Blueprint('list', __name__)


def serialize_shopping_list(shopping_list):
    return {
        'id': shopping_list.id,
        'created': shopping_list.created,
        'updated': shopping_list.updated,
        'user_id': shopping_list.user_id
    }


def serialize_shopping_list_item(shopping_list_item):
    return {
        'id': shopping_list_item.id,
        'created': shopping_list_item.created,
        'updated': shopping_list_item.updated,
        'shopping_list_id': shopping_list_item.shopping_list_id,
        'name': shopping_list_item.name,
        'category': shopping_list_item.category,
        'quantity': shopping_list_item.quantity,
        'finished': shopping_list_item.finished
    }


@shopping_lists_api.route('/add_shopping_list/<user_id>', methods=['POST'])
@check_for_token
def add_shopping_list(user_id):
    new_shopping_list = ShoppingList(user_id=user_id)
    db.session.add(new_shopping_list)
    db.session.commit()
    return serialize_shopping_list(new_shopping_list), 200


@shopping_lists_api.route('/get_shopping_lists/<user_id>', methods=['GET'])
@check_for_token
def get_shopping_lists(user_id):
    shopping_lists = ShoppingList.query.filter_by(user_id=user_id)
    return jsonify(list(map(serialize_shopping_list, shopping_lists))), 200


@shopping_lists_api.route('/add_shopping_list_item/<shopping_list_id>', methods=['POST'])
@check_for_token
def add_shopping_list_item(shopping_list_id):
    body = json.loads(request.data)
    new_shopping_list_item = ShoppingListItem(name=body['name'], category=body['category'], quantity=body['quantity'],
                                              shopping_list_id=shopping_list_id)
    db.session.add(new_shopping_list_item)
    db.session.commit()
    return serialize_shopping_list_item(new_shopping_list_item), 200


@shopping_lists_api.route('/get_shopping_list_items/<shopping_list_id>', methods=['GET'])
@check_for_token
def get_shopping_list_items(shopping_list_id):
    shopping_list_items = ShoppingListItem.query.filter_by(shopping_list_id=shopping_list_id)
    return jsonify(list(map(serialize_shopping_list_item, shopping_list_items))), 200
