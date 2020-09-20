from flask import Flask
from configs.db_config import *

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_username}:{db_pwd}@{db_host}/{db_name}"

if __name__ == '__main__':
    from routers.user_routers import users_api

    application.register_blueprint(users_api)
    application.run(debug=True)
