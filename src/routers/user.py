import json
import hashlib

from flask import Blueprint, request

from configs.token_config import check_for_token
from models.user import User
from application import db

users_api = Blueprint('users', __name__)


def md5_password(password):
    return hashlib.md5(password.encode('utf8')).hexdigest()


@users_api.route('/users')
@check_for_token
def get_users():
    return 'users', 200


@users_api.route('/add_user', methods=['POST'])
def add_user():
    body = json.loads(request.data)
    new_user = User(email=body["email"], password=md5_password(body["password"]))
    db.session.add(new_user)
    db.session.commit()
    return '', 200


@users_api.route('/update_user/<user_id>', methods=['PUT'])
@check_for_token
def update_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return {'error': 'user not found'}, 404
    body = json.loads(request.data)

    if 'email' in body:
        user.email = body.get('email')

    if 'password' in body:
        user.password = md5_password(body.get('password'))

    db.session.commit()

    return {'message': 'user updated'}, 200
