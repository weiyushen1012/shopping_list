from flask import Blueprint

users_api = Blueprint('users', __name__)


@users_api.route('/users')
def get_users():
    return 'users', 200
