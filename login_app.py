import flask
from flask import redirect, url_for
import flask_login

from blueprint.secret import secret_bp
from model.user import User

login_manager = flask_login.LoginManager()

app = flask.Flask(__name__)
app.register_blueprint(secret_bp, url_prefix="/secret")

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == "GET":
        return "<form action='/login' method='POST'><input type='text' name='user'><button type='submit'>Submit</button></form>"

    user = flask.request.form.get('user')
    if user == "user":
        # Login and validate the user.
        # user should be an instance of your `User` class
        flask_login.login_user(user)

        flask.flash('Logged in successfully.')

        return flask.redirect(next or flask.url_for('index'))
    return flask.redirect(flask.url_for('login'))

@app.route('/admin')
def admin():
    return "Admin page"

@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return redirect(url_for('login'))