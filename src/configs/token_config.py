import jwt
import os
from functools import wraps
from flask import request

SECRET_KEY = os.environ.get('SHOPPING_LIST_SECRET_KEY')
TOKEN_EXPIRES = int(os.environ.get('SHOPPING_LIST_TOKEN_EXPIRES')) if os.environ.get(
    'SHOPPING_LIST_TOKEN_EXPIRES') is not None else 0


def check_for_token(func):
    @wraps(func)
    def wrapped(*args, **kwargs):

        token = request.args.get('token')
        if not token:
            return {'message': 'Missing token'}, 403
        try:
            payload = jwt.decode(token, SECRET_KEY)
            jwt_user_id = payload['user_id']

            if 'user_id' in kwargs and int(jwt_user_id) != int(kwargs['user_id']):
                return {'message': 'Unauthorized user access'}, 403
        except:
            return {'message': 'Invalid token'}, 403
        return func(*args, **kwargs)

    return wrapped
