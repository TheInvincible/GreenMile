from datetime import datetime
from green import db, login_manager # login_manager
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash


login_manager = LoginManager

def create_app(config_name):
    # existing code remains

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
    	return User.query.get(int(user_id))
    
    return app


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	company_id = db.Column('Company', db.Integer, db.ForeignKey('company.id'))
	role_id = db.Column('Role', db.Integer, db.ForeignKey('role.id'))
	is_admin = db.Column(db.Boolean, default=False)

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute.')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return f"User('{self.username}', '{self.image_file}'"




class Role(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), unique=True, nullable=False)
	description = db.Column(db.String(200))
	user = db.relationship('User', backref='role', lazy=True)

	def __repr__(self):
		return '<Roles: {}>'.format(self.name)


class Company(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), unique=True, nullable=False)
	description = db.Column(db.String(200))
	user = db.relationship('User', backref='company', lazy=True)

	def __repr__(self):
		return '<Company: {}>'.format(self.name)
# class Update(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	title = db.Column(db.String(100), nullable=False)
# 	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
# 	content = db.Column(db.Text, nullable=False)
# 	user_id = db.Column(db.Integer, db.ForeignKey(user.id), nullable=False)

# 	def __repr__(self):
# 		return f"Post('{self.title}', {self.date_posted}')"


if __name__ == '__main__':
	db.create_all()