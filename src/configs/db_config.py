import os

db_username = os.environ.get("SHOPPING_LIST_APP_DB_USERNAME")
db_pwd = os.environ.get("SHOPPING_LIST_APP_DB_PASSWORD")
db_host = os.environ.get("SHOPPING_LIST_APP_DB_HOST")
db_name = os.environ.get("SHOPPING_LIST_APP_DB_NAME")


def register_db(application):
    application.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_username}:{db_pwd}@{db_host}/{db_name}"
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
