from flask import Blueprint

home_api = Blueprint('home', __name__)


@home_api.route('/')
def home():
    return 'Shopping list API', 200
