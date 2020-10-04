import datetime
import jwt
import json

from flask import Blueprint, request

from configs.token_config import SECRET_KEY, check_for_token, TOKEN_EXPIRES
from models.user import User
from routers.user import md5_password

auth_api = Blueprint('auth', __name__)


@auth_api.route('/login', methods=['POST'])
def login():
    email = json.loads(request.data)["email"]
    password = json.loads(request.data)["password"]

    user = User.query.filter_by(email=email).first()

    if user is not None and md5_password(password) == user.password:
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=TOKEN_EXPIRES)
        },
            SECRET_KEY)
        return {'token': token.decode('utf-8'), 'userId': user.id, "email": email}
    else:
        return {'message': 'Invalid email or password'}, 403


@auth_api.route('/refresh_token/<user_id>', methods=['GET'])
@check_for_token
def refresh_token(user_id):
    token = jwt.encode({
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=TOKEN_EXPIRES)
    },
        SECRET_KEY)
    return {'token': token.decode('utf-8')}
