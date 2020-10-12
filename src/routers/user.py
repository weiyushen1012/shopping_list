import json
import hashlib
from datetime import datetime

from flask import Blueprint, request, jsonify

from configs.token_config import check_for_token
from models.user import User
from models.init import db

users_api = Blueprint('users', __name__)


def md5_password(password):
    return hashlib.md5(password.encode('utf8')).hexdigest()


def serialize_user(user):
    return {
        'id': user.id,
        'email': user.email,
        'created': user.created,
        'updated': user.updated
    }


@users_api.route('/get_users', methods=['GET'])
@check_for_token
def get_users():
    users = User.query.all()
    return jsonify(list(map(serialize_user, users))), 200


@users_api.route('/add_user', methods=['POST'])
def add_user():
    body = json.loads(request.data)
    new_user = User(email=body["email"], password=md5_password(body["password"]))
    db.session.add(new_user)
    db.session.commit()
    return serialize_user(new_user), 200


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

    user.updated = datetime.utcnow()

    db.session.commit()

    return {'message': 'user updated', 'user': serialize_user(user)}, 200
