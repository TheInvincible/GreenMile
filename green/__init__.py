from flask import Flask # Importing the Flask class from flask framework
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy # Importing the SQL database from the sqlalchemy package
from flask_login import LoginManager
import psycopg2
from psycopg2 import Error


# from config import Config
# app.config['DEBUG'] = True
from config import app_config

db = SQLAlchemy() # the sqlalchemy instance
login_manager = LoginManager()
def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)  # Setting the name of the current flask module to an instance of the Flask class (Instantiate a flask application into a variable(app variable in this case))
	# app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	
	Bootstrap(app)
	db.init_app(app)

	login_manager.init_app(app)
	login_manager.login_message = "You must be logged in to access this page!"
	login_manager.login_view = "auth.login"
	migrate = Migrate(app, db)

	from green import models
	from green.logic.admin import admin as admin_blueprint
	app.register_blueprint(admin_blueprint, url_prefix='/admin')

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

    


