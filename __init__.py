from flask import Flask
from flask_sqlalchemy import SQLAlchemy

my_database = SQLAlchemy()
DATABASE_NAME = "database.my_database"
DATABASE_USER = "ghandylan"
DATABASE_PASSWORD = "hotdog123"

def createApp():
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = 'mysecret'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}"
    my_database.init_app(app)

    from views import views
    from auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app