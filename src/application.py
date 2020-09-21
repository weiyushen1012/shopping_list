from flask import Flask
from configs.db_config import *
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/shopping_list')
load_dotenv(os.path.join(project_folder, '.env'))

application = Flask(__name__)
# CORS(application, resources={r"/*": {"origins": "http://localhost:63343"}})
CORS(application)

application.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_username}:{db_pwd}@{db_host}/{db_name}"
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)


@application.route('/')
def home():
    return 'Shopping list API', 200


if __name__ == '__main__':
    from routers.user import users_api
    from routers.auth import auth_api

    application.register_blueprint(users_api)
    application.register_blueprint(auth_api)

    application.run(debug=True)
