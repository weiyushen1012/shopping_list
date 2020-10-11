import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_migrate import Migrate

from configs.db_config import register_db

from models.init import db

from routers.home import home_api
from routers.user import users_api
from routers.auth import auth_api
from routers.shopping_list import shopping_lists_api

project_folder = os.path.expanduser('~/shopping_list')
load_dotenv(os.path.join(project_folder, '.env'))

application = Flask(__name__)
CORS(application)
register_db(application)

db.init_app(application)

migrate = Migrate(application, db)

application.register_blueprint(users_api)
application.register_blueprint(auth_api)
application.register_blueprint(home_api)
application.register_blueprint(shopping_lists_api)

if __name__ == '__main__':
    application.run(debug=True)
