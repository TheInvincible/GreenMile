from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user

from . import authent
from .forms import LoginForm
from ...import db
from ...models import User
from .. import admins


@authent.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect_url('home/dashboard.html')
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.get(form.username.data)
		if user:
			if bcrypt.check_password_hash(user.password, form.password.data):
				user.is_admin = True
				db.session.add(user)
				db.session.commit()
				login_user(user, remember=True)
				return redirect(url_for('home/dashboard.html'))
		else:
			flash('Invalid username or password')
	return render_template('authent/login.html', form=form, title='Login')


@authent.route('/logout')
@login_required
def logout():
	user = current_user
	user.is_admin = False
	db.session.add(user)
	db.session.commit()
	logout_user()
	flash('You have successfully been logged out.')

	return redirect(url_for('authent/login.html'))
