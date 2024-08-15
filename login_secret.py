from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flask_login import login_required

secret_bp = Blueprint('secret', __name__,
                        template_folder='templates')

@secret_bp.route('/noneed')
def no_need():
    return "You can see this without login."

@secret_bp.route('/needlogin')
@login_required
def show():
    return "can't see this if not login"
