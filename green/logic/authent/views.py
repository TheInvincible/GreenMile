from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user

from . import authent
from .forms import LoginForm
from ...import db
from ...models import User


@authent.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect_url('home/home.dashboard')
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is not None and employee.verify_password(form.password.data):
			login_user(user)
			return redirect(url_for('home/home.dashboard'))
		else:
			flash('Invalid username or password')
	return render_template('authent/login.html', form=form, title='Login')


@authent.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have successfully been logged out.')

	return redirect(url_for('authent/login.html'))
