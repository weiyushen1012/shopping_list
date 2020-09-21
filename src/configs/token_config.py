import jwt
import os
from functools import wraps
from flask import request

SECRET_KEY = os.environ.get('SHOPPING_LIST_SECRET_KEY')


def check_for_token(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return {'message': 'Missing token'}, 403
        try:
            jwt.decode(token, SECRET_KEY)
        except:
            return {'message': 'Invalid token'}, 403
        return func(*args, **kwargs)

    return wrapped
