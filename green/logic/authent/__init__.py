from flask import Blueprint

authent = Blueprint('authent', __name__)

from . import views