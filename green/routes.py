from green import app
from flask import render_template, url_for, flash, redirect
from green.forms import LoginForm
from green.models import User
from flask_login import login_user, current_user, login_required, logout_user

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/admin')
def dashboard():
	return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.username.data == 'admin' and form.password.data == 'password':
			flash(f'Welcome {form.username.data}!', 'alert-success')
			return redirect(url_for('dashboard'))
		else:
			flash('Login Unsuccessful. Please check your details', 'alert-danger')
	return render_template('login.html', title='Login', form=form)