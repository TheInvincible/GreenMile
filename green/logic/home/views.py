from flask import render_template
from flask_login import login_required

from . import home as viola


@viola.route('/')
@viola.route('/home')
def home():
	return render_template('home/home.html', title='Home')

@viola.route('/dashboard')
@login_required
def dashboard():
	return render_template('home/dashboard.html', title='Dashboard')


