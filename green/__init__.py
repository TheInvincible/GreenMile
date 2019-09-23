from flask import Flask # Importing the Flask class from flask framework
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy # Importing the SQL database from the sqlalchemy package
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import psycopg2
from psycopg2 import Error
from flask_admin import Admin, BaseView
from flask_admin.contrib.sqla import ModelView


SECRET_KEY = 'ee74cfafc19495358de8ba756ce6746a'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1Superuser!2@localhost:5432/greenmiledb'
# app.config['DEBUG'] = True
from config import app_config

db = SQLAlchemy() # the sqlalchemy instance
login_manager = LoginManager()

def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)  # Setting the name of the current flask module to an instance of the Flask class (Instantiate a flask application into a variable(app variable in this case))
	app.config.from_pyfile('config.py')

	admin = Admin(app)

	Bootstrap(app)
	db.init_app(app)

	bcrypt = Bcrypt(app)

	login_manager.init_app(app)
	login_manager.login_message = "You must be logged in to access this page!"
	login_manager.login_view = "authent.login"
	migrate = Migrate(app, db)

	from green.models import User

	admin.add_view(ModelView(User, db.session))	

	from green import models
	from green.logic.admins import admins as admins_blueprint
	app.register_blueprint(admins_blueprint, url_prefix='/admin')

	from green.logic.authent import authent as authent_blueprint
	app.register_blueprint(authent_blueprint)

	from green.logic.home import home as home_blueprint
	app.register_blueprint(home_blueprint)


  # importing our routes and models
	# from green.models import db

	# manager = Manager(app)

	# manager.add_command('db', MigrateCommand)
	# manager.run()

	return app



