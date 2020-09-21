import datetime
import jwt
import json

from flask import Blueprint, session, request

from configs.token_config import SECRET_KEY
from models.user import User
from routers.user import md5_password

auth_api = Blueprint('auth', __name__)


@auth_api.route('/login', methods=['POST'])
def login():
    email = json.loads(request.data)["email"]
    password = json.loads(request.data)["password"]

    user = User.query.filter_by(email=email).first()

    if user is not None and md5_password(password) == user.password:
        session.login = True
        token = jwt.encode({
            'user': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
        },
            SECRET_KEY)
        return {'token': token.decode('utf-8')}
    else:
        return {'message': 'Invalid email or password'}, 403
