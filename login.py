
from database import db
from flask import render_template
from flask.blueprints import Blueprint

dbinstance = Blueprint('dbinstance', __name__,

                 template_folder='templates',
                 static_folder='static')
                 
#from model import Base
import bcrypt

import os

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.inspection import inspect
from sqlalchemy.dialects import postgresql
#from sqlalchemy import db.db.mapped_column, Table, Column, Bigdb.Integer, db.Integer, db.db.Text, db.Date, db.Boolean, db.db.String, ForeignKey
from sqlalchemy import desc
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, func, cast, Float 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship,scoped_session,sessionmaker,aliased

engine = db 
Session = sessionmaker(bind=engine) 
session = Session()  

@dbinstance.route('/login')
# ‘/login’ URL is bound with login() function.
def login():
    """
    Render the login page.

    Thisfunction chceks whether the user is already logged-in. If user is logged in,
    it redirects them to cart page.If the user arrived at the login page after registration,
    they will see a registration success message.

    Returns:
        A rendered template of 'login.html'. If the user is logged in, it may also redirect
        them to the cart page. If the user arrived after registration,
        they will see a success message.
    """
    # check whether user is logged or not
    username = session['user_details']['id']
    #username = session['user']['id']
    if username in session:
        return redirect(url_for('cart'))  # redirect to cart page if user is already logged
    registered = request.args.get('registered')  # get registered url parameter
    error_msg = request.args.get('error_msg')  # get registered url parameter

    #  if user landed to loging page after registraion, user will see a regisration success message
    if registered:
        return render_template('login.html',
                               success_message='You have successfully been registered. please login...')
    if error_msg:
        return render_template('login.html',
                               error_message=error_msg)
    return render_template('login.html')
    

class UserDetails(db.Model):
    __tablename__ = 'user_details'
    id = db.Column(db.Integer, db.Sequence('user_id_seq'), primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(64), nullable=False)

    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
