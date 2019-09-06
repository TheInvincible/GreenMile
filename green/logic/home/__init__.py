from flask import Blueprint

home = Blueprint('home', __name__)

from green.logic.home import views