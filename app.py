"""
Module docstring: This module provides functionality
for Cellmart wesite developed using flask.
"""
import sys
import platform
import flask
import re
import logging
import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from db_init import db
from docxtpl import DocxTemplate
from flask import Response
from io import BytesIO
from flask import Flask, send_file

from datetime import datetime
from flask import Flask, request, redirect, url_for, session, flash
from flask import render_template
from db_init import create_app
from db_init import db
from model import UserDetails, Product, OrderDetails, TParceldem, TCom2023, TCadastre, TPub, TUsager, TDemande, Country, City, Customer

from sqlalchemy.sql import text
from sqlalchemy import desc, asc, and_, select
from model import Base

import flask
import flask_login
from flask import Blueprint
from flask_login import LoginManager
from flask import Flask, render_template
from flask_htmx import HTMX
#Base = db.session.query

# Create the logger
logger = logging.getLogger('failed_login_attempts')
logger.setLevel(logging.INFO)

# Create a file handler
handler = logging.FileHandler('failed_login_attempts.log')
logger.addHandler(handler)
'''
app = create_app(os.getenv("CONFIG_MODE"))
app.secret_key = '12345678'
'''
from database import db
from flask import render_template
from flask.blueprints import Blueprint


dbinstance = Blueprint('dbinstance', __name__,

                 template_folder='templates',
                 static_folder='static')
                 
   
#from database import db
from flask import Flask
import os.path

#from home import dbinstance
#from home import UserDetails

from book_list import dbinstance
from book_list import book_list

from export_pandas_excel import dbinstance
from export_pandas_excel import export_pandas_excel

from excel_pivot_conc import dbinstance
from excel_pivot_conc import excel_pivot_conc

from excel import dbinstance
from excel import excel

from login import dbinstance
from login import UserDetails

'''
from periode import dbinstance
from dossier import dbinstance
#from dossier import TDemande
from dossier import TUsager
from tdem import dbinstance
from tdem import TDemande
from tpub import dbinstance
from tpub import TPub
'''
from dossier import dbinstance
from dossier import TDemande
from dossier import TUsager

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, func, cast, Float 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship,scoped_session,sessionmaker,aliased

from flask import Flask, render_template, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy  
from wtforms import SelectField
from flask_wtf import FlaskForm

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = os.getenv("FLASK_DEBUG")
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DEVELOPMENT_DATABASE_URL")
    app.config['SQLALCHEMY_ECHO'] = True
    '''
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI']) 
    Session = sessionmaker(bind=engine) 
    session = Session()     
    '''
    '''
    login_manager = LoginManager()
    login_manager.init_app(app)

@LoginManager.user_loader
def load_user(user_id):
    x = Users.query.get(str(user_id))
    if x == None:
        x = Admins.query.get(str(user_id))
    return x

    login_manager.blueprint_login_views = {
        'home': '/',
        'login': '/login',
    }
    '''
    '''
    login_manager = LoginManager()
    #Added this line fixed the issue.
    login_manager.init_app(app) 
    #login_manager.login_view = 'users.login'
    #login_manager.login_view = 'login'
    '''
    db.init_app(app)
    
    app.register_blueprint(dbinstance, url_prefix='')
    
    #import home
    import book_list
    import export_pandas_excel
    import excel_pivot_conc
    import excel
    import login
    '''
    import laperiode
    import periode

    import tpub
    import tdem 
    '''
    import dossier
    app.add_url_rule('/', view_func=login.login)
    #app.add_url_rule('/home', view_func=home.home)
    #app.add_url_rule('/login', view_func=login.login)
    '''
    app.add_url_rule('/laperiode', view_func=periode.date)
    app.add_url_rule('/periode', view_func=periode.periode)
    app.add_url_rule('/getdossier', view_func=dossier.getdossier)
    app.add_url_rule('/tpub', view_func=tpub.tpub)
    app.add_url_rule('/tdem', view_func=tdem.tdem)
    '''
    app.add_url_rule('/book_list', view_func=book_list.book_list)
    app.add_url_rule('/export_pandas_excel', view_func=export_pandas_excel.export_pandas_excel)
    app.add_url_rule('/excel_pivot_conc', view_func=excel_pivot_conc.excel_pivot_conc)
    app.add_url_rule('/excel', view_func=excel.excel)
    app.add_url_rule('/dossier', view_func=dossier.dossier)



    cache.init_app(app)
    return app 

from flask_caching import Cache
cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
#from .cache import cache
    
def setup_database(app):
    with app.app_context():
        db.create_all()

from werkzeug.debug import DebuggedApplication
'''
def create_app():
    # Insert whatever else you do in your Flask app factory.

    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    return app
'''    
class Form(FlaskForm):

    commune = SelectField('commune', choices=[])
    section = SelectField('section', choices=[])
    parcelle = SelectField('parcelle', choices=[])
 

@dbinstance.route('/section/<get_section>')
def sectionbycommune(get_section):
    #section = TCadastre.query.distinct(TCadastre.ccosec).filter_by(idcom=get_section).all()
    section = db.session.query(TCadastre).distinct(TCadastre.ccosec).filter_by(idcom=get_section).all()
    #form.commune.default = [('0', '-- select an option --')] + section
    sectionArray = []
    for parcelle in section:
        sectionObj = {}
        sectionObj['ccosec'] = parcelle.ccosec
        sectionObj['idsuf'] = parcelle.idsuf
        sectionObj['idcom'] = parcelle.idcom
        sectionArray.append(sectionObj)
    return jsonify({'sectioncommune' : sectionArray})
  
@dbinstance.route('/parcelle/<get_parcelle>')
def parcelle(get_parcelle):
    section_data = db.session.query(TCadastre).filter_by(ccosec=get_section).all()
    parcelleArray = []
    for parcelle in section_data:
        parcelleObj = {}
        parcelleObj['ccosec'] = parcelle.ccosec
        parcelleObj['idsuf'] = parcelle.idsuf        
        parcelleObj['idcom'] = parcelle.idcom
        parcelleArray.append(parcelleObj)
    return jsonify({'parcellelist' : parcelleArray}) 
  


def get_dossier():
    if 'user' in session:
        user_id = session['user']['id']
        no_interne = request.form.get('no_interne')
    #return db.session.query(OrderDetails).all()
        flash('test :' , str(no_interne))
        print('order_id:', str(no_interne))
        return db.session.query(TDemande).where(TDemande.no_interne == str(no_interne))
    return db.session.query(TDemande).where(TDemande.no_interne == str(no_interne))    
    #nointerne = request.form.get('selected_class')
    #return(str(nointerne))
    #return db.session.query(TDemande).where(TDemande.no_interne == str(nointerne))

def get_fiche():
    if 'user' in session:
        user_id = session['user']['id']
        order_id = request.form.get('order_id')
    #return db.session.query(OrderDetails).all()
        flash('test :' , str(order_id))
        print('order_id:', str(order_id))
        return db.session.query(OrderDetails).where(OrderDetails.id == str(order_id))
    return db.session.query(OrderDetails).where(OrderDetails.id == str(order_id))    
    #nointerne = request.form.get('selected_class')
    #return(str(nointerne))
    #return db.session.query(TDemande).where(TDemande.no_interne == str(nointerne))

@dbinstance.route('/fiche')
def fiche():
    #orders = get_all_order_details()
    orders = get_fiche()
    if 'user' in session:
        # if user has a active session get the username from the session
        name = session['user']['name']
        username = session['user']['id']
        order_id = request.form.get('order_id')
        user_orders = fetch_orders_by_id(username)
        return render_template('fiche.html', username=name, orders=user_orders)
    # return login page to the user if user does not have an active session
    return redirect(url_for('login'))

'''
@dbinstance.route('/getdossier', methods=['GET', 'POST'])
def getdossier():
    #orders = get_all_order_details()
    #dossiers = get_all_t_demande()
    dossiers = get_dossier()
    if request.method == 'POST' :
#    or request.method == 'GET' :
# Get the order details from the form
        user_id = session['user']['id']
        no_interne = request.form.get('no_interne')
        product_name = request.form.get('product_name')
        no_interne = fetch_dossiers_by_no_interne(no_interne)
        #user_orders = fetch_orders_by_id(user_id)
        #quantity = int(request.form.get('quantity'))
        #product = get_product_by_id(product_id)
        #price = float(product.price)
        #total = price * quantity
        flash('test :' , str(no_interne))
        print('id:', str(no_interne))
        # Save the order details to the DB
        #name = session['user']['name']
        #order_details = OrderDetails(username=user_id, id=order_id)
        #user_orders = fetch_orders_by_id(userId)
        fv = flask.__version__
        pv = platform.python_version()
        return render_template('dossier.html', fv=fv, pv=pv, dossiers=no_interne, username=user_id)

        #db.session.add(order_details)
        db.session.commit()

    return redirect(url_for('dossier'))
''' 
        

@dbinstance.route('/getfiche', methods=['GET', 'POST'])
def getfiche():
    #orders = get_all_order_details()
    orders = get_fiche()
    if request.method == 'POST' :
#    or request.method == 'GET' :
# Get the order details from the form
        user_id = session['user']['id']
        order_id = request.form.get('order_id')
        product_name = request.form.get('product_name')
        user_orders = fetch_orders_by_order_id(order_id)
        #user_orders = fetch_orders_by_id(user_id)
        #quantity = int(request.form.get('quantity'))
        #product = get_product_by_id(product_id)
        #price = float(product.price)
        #total = price * quantity
        flash('test :' , str(order_id))
        print('id:', str(order_id))
        # Save the order details to the DB
        #name = session['user']['name']
        #order_details = OrderDetails(username=user_id, id=order_id)
        #user_orders = fetch_orders_by_id(userId)
        return render_template('fiche.html', id=order_id, username=user_id, orders=user_orders)

        #db.session.add(order_details)
        db.session.commit()

    return redirect(url_for('fiche'))


def fetch_dossiers_by_no_interne(no_interne):
    """
    Fetch orders from the database by user ID.

    Args:
        user_id (int): The ID of the user to fetch orders for.

    Returns:
        list: A list of orders for the given user ID.
    """
    dossiers = db.session.query(TDemande, TUsager
        ).filter(TDemande.no_interne == no_interne
        ).join(TUsager, TUsager.u_pacage == TDemande.no_pacage_demandeur
        ).with_entities(TDemande.no_interne, TDemande.date_de_depot,\
        TDemande.no_pacage_demandeur, TUsager.u_nom_raison_sociale 
        ).all()
    dossiers_list = []
    for dossier in dossiers:
        dossiers_list.append({
            'no_interne': dossier.no_interne,
            'date_de_depot': dossier.date_de_depot,
            'no_pacage_demandeur': dossier.no_pacage_demandeur,
            'u_nom_raison_sociale': dossier.u_nom_raison_sociale
        })

    return dossiers_list



from sqlalchemy import desc
#someselect.order_by(desc(table1.mycol))

def fetch_dossiers_by_id(user_id):
    """
    Fetch orders from the database by user ID.

    Args:
        user_id (int): The ID of the user to fetch orders for.

    Returns:
        list: A list of orders for the given user ID.
    """
    dossiers = TDemande.query.filter_by(user_id=user_id).order_by(desc(TDemande.no_interne)).all()

    dossiers_list = []
    for dossier in dossiers:
        dossiers_list.append({
            'no_interne': dossier.no_interne,
            'date_de_depot': dossier.date_de_depot
        })

    return dossiers_list


def fetch_orders_by_id(user_id):
    """
    Fetch orders from the database by user ID.

    Args:
        user_id (int): The ID of the user to fetch orders for.

    Returns:
        list: A list of orders for the given user ID.
    """
    orders = OrderDetails.query.filter_by(username=user_id).all()

    orders_list = []
    for order in orders:
        orders_list.append({
            'id': order.id,
            'username': order.username,
            'product_id': order.product_id,
            'delivery_address': order.delivery_address,
            'product_name': order.product_name,
            'quantity': order.quantity,
            'price': order.price,
            'total': order.total
        })

    return orders_list

 
def fetch_orders_by_order_id(order_id):
    """
    Fetch orders from the database by user ID.

    Args:
        user_id (int): The ID of the user to fetch orders for.

    Returns:
        list: A list of orders for the given user ID.
    """
    orders = OrderDetails.query.filter_by(id=order_id).all()

    orders_list = []
    for order in orders:
        orders_list.append({
            'id': order.id,
            'username': order.username,
            'product_id': order.product_id,
            'delivery_address': order.delivery_address,
            'product_name': order.product_name,
            'quantity': order.quantity,
            'price': order.price,
            'total': order.total
        })

    return orders_list


def get_product_by_id(product_id):
    return db.session.query(Product).get(product_id)

def get_parcelle_by_idsuf(idsuf):
    return db.session.query(TCadastre).get(idsuf)

def get_all_t_demande():
    return db.session.query(TDemande).all()

def get_all_products():
    return db.session.query(Product).all()

def get_all_parcelles():
    return db.session.query(TCadastre).filter(TCadastre.idsuf.like("99999%")).all()

def get_all_parceldem():
    return db.session.query(TParceldem).filter(TParceldem.par_nointerne.like("C22160001")).all()

def get_all_t_com2023():
    return db.session.query(TCom2023).filter(TCom2023.dep == '22').all()

    
def fetch_sections_by_commune(idcom):
    sections = db.session.query(TCadastre.ccosec.distinct()).where(TCadastre.idcom=='22278').all()

    sections_list = []
    for section in sections:
        sections_list.append({
            #'idcom': request.form['res'],
            'ccosec': TCadastre.ccosec
            #'idsuf': TCadastre.idsuf
        })

    return sections_list

def get_all_order_details():
    if 'user' in session:
        user_id = session['user']['id']
    #return db.session.query(OrderDetails).all()
        return db.session.query(OrderDetails).filter(OrderDetails.username == user_id)
    return db.session.query(OrderDetails).filter(OrderDetails.username == 0)    
    #return redirect(url_for('login'))
    #return db.session.query(OrderDetails).order_by("Order_Details.id desc")
    #return db.session.query(OrderDetails).order_by(desc(OrderDetails.id))

# this method authenticate user with username and password
def authenticate_user(email, password):
    """
    Authenticates user with email & password.

    This method chec if the provided email and password match any users
    credentials stored in DB

    Args:
        email (str):  email to authenticate.
        password (str): password to authenticate.

    Returns:
       user:  if the email and password match, ifnot otherwise.
    """

    # Retrieve the user details based on the provided email
    user = UserDetails.query.filter_by(email=email).first()

    # Check if a user with the provided email exists and if the password matches
    if user and user.check_password(password):
        return {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'role': user.role
        }
    else:
        return None


def insert_default_products():
    default_products = [
        {"id": 1, "name": "iphone 15 pro", "price": 1199.0, "image_name": "iphone-15-pro.png"},
        {"id": 2, "name": "Oneplus 9", "price": 799.0, "image_name": "oneplus-9.png"},
        {"id": 3, "name": "Samsung S24 ultra", "price": 1299.0, "image_name": "s24-ultra.png"},
        {"id": 4, "name": "Xiaomi mi 11", "price": 599.0, "image_name": "xiaomi-mi-11.png"},
        {"id": 5, "name": "iPhone 13 pro", "price": 1000.0, "image_name": "iphone 13 pro.jpeg"}
    ]

    for product in default_products:
        existing_product = Product.query.filter_by(id=product["id"]).first()
        if not existing_product:
            new_product = Product(
                id=product["id"],
                name=product["name"],
                price=product["price"],
                image_name=product["image_name"]
            )
            db.session.add(new_product)
    db.session.commit()



@dbinstance.route('/',methods=["POST","GET"])
# ‘/’ URL is bound with home() function.
def home():   
    t_parceldem = get_all_parceldem()
    order_details = get_all_order_details()
    products = get_all_products()
    t_com2023 = get_all_t_com2023()
    parcelles = get_all_parcelles()
    #com='search_com2023_id'
    sections = fetch_sections_by_commune('22278')
   
    fv = flask.__version__
    pv = platform.python_version()
    # check whether user is logged or not
    
    form = Form()
    form.commune.choices = [(commune.com, commune.libelle) for commune in db.session.query(TCom2023).filter_by(dep='22').all()]

    # Import cache
    # store a value
    #cache.set("my_value", 1_000_000)

    # Get a value
    #my_value = cache.get("my_value")
  
    if 'user' in session:
        
        if request.method == 'POST':
            
            cache.set("commune", str(""))
            cache.set("section", str(""))
            cache.set("parcelles", str(""))

            #parcelle = db.session.query(TCadastre).filter_by(idcom=form.parcelle.data).first()
            commune = db.session.query(TCom2023).filter_by(com=form.commune.data).first()
            cache.set("commune", db.session.query(TCom2023).filter_by(com=form.commune.data).first())
            section = db.session.query(TCadastre).filter_by(ccosec=form.section.data).first()
            cache.set("section", db.session.query(TCadastre).filter_by(ccosec=form.section.data).first())
            #parcelles = db.session.query(TCadastre.idsuf).where(and_((TCadastre.idcom==format(commune.com),(TCadastre.ccosec==format(section.ccosec))))).all()
            parcelles = db.session.query(TCadastre.idsuf).where(and_((TCadastre.idcom==commune.com),(TCadastre.ccosec==section.ccosec))).all()
            cache.set("parcelles", db.session.query(TCadastre.idsuf).where(and_((TCadastre.idcom==commune.com),(TCadastre.ccosec==section.ccosec))).all())
            #parcelles = db.session.query(TCadastre.idsuf).where((TCadastre.idcom==format(commune.com)) | (TCadastre.ccosec==format(section.ccosec))).all()            
            '''
            parcelles_list = []
            for parcelle in TCadastre:
                parcelles_list.append({
                #'idcom': request.form['res'],
                'idsuf': TCadastre.idsuf
                })
            return parcelles_list
            '''
            #return '<h1>commune : {}, section: {}, parcelle: {}</h1>'.format(commune.libelle, section.ccosec, '')
        #return render_template('index.html', form=form)
        '''
        return render_template('index.html', form=form, pv=pv, fv=fv, username=session[
        'user']['name'], order_details=order_details, products=products,
        t_com2023=t_com2023, sections=sections, parcelle='223580000A1009BK',
        commune='TREGONNEAU', section='A')  # return index.html with username of logged user
        #parcelle='223580000A1009BK', commune='TREGONNEAU', section='A'
        #, parcelle=parcelle, commune=commune, section=section
        '''
        return render_template('index.html', t_parceldem=t_parceldem, parcelles=parcelles, form=form, pv=pv, fv=fv, username=session[
            'user']['name'], order_details=order_details, products=products)  # return index.html with username of logged user

    return redirect(url_for('dbinstance.login'))


def header():
    #pv = print(sys.version)
    #pv = print(platform.python_version())
    fv = flask.__version__
    pv = platform.python_version()
    return render_template('header.html', fv=fv, pv=pv)  # return index.html with username of logged user

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
    if 'username' in session:
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


@dbinstance.route('/about')
def about():
    t_demande = get_all_t_demande()
    if 'user' in session:
        return render_template('about.html', username=session[
            'user']['name'], t_demande=t_demande)

    return render_template('about.html')
 

@dbinstance.route('/login', methods=['POST'])
# ‘/login’ URL is bound with login_action() function.
def login_action():
    """
    Perform login action.

    This fnuction is bound to the '/login' URL and handles POST requests.
    It retrieves the email and password from the request form, attempts to authenticate
    the user, and if successful, saves the email in the session and redirects the user to
    the cart page. If the authentication fails, it rendres the login page again with an
    error message indicating invalid login credentials.

    Returns:
        If authentication is successful, redirects the user to the cart page.
        If authentication fails, renders the 'login.html' template with an error message.

    Raises:
        An erro: If 'email' or 'password' fields are missing in the request form.
    """
    #  get email and password from request
    email = request.form['email']
    password = request.form['password']
    #authenticate user and if login credentials are valid save email in
    #session and redirect user to cart page

    logged_user = authenticate_user(email, password)

    if logged_user:
        session['user'] = logged_user  # Store email in session
        return redirect(url_for('dbinstance.home'))

    # Log the failed login attempt
    ip_address = request.remote_addr
    logger.info("Failed login attempt for EMAIL :: %s from IP :: %s address at TIME :: %s",
                email, ip_address, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    #show an error message to the user if login credentials are not valid.
    return render_template('login.html', email=email, password=password,
                           error_message='Authentification invalide ! Merci de bien vouloir vérifier votre adresse de courriel, votre mot de passe et de refaire une tentative de connection.')


@dbinstance.route('/register', methods=['GET'])
# ‘/register’ URL is bound with register() function.
def register():
    """
    Render the registrtion page.

    This function checks whether the user is already logged in. If the usr is logged in,
    it redirects them to the cart page. If the user is not logged in, it renders registration
    page where the user can signup for a account.

    Returns:
        A rendered template of 'register.html'. If the user is already logged in,
        it may also redirect
        them to the cart page.
    """
    # check whether user is logged or not
    if 'user' in session:
        return redirect(url_for('home'))  # redirect to cart page if user is already logged
    #  return registration page tp the user if user has no any active sessions
    return render_template('register.html')


@dbinstance.route('/register', methods=['POST'])
# ‘/register’ URL is bound with register_action() function.
def register_action():
    """
    Register new user.

    This function receives a POST request with user registration data,
    including name, email, and password. It checks if the provided
    email already exists in the system and, if the password
    meets the complexity requirements. If all checks pass, the user
    details are stored in DB for registration completion.
    If there are any errors, such as duplicate username/email or
    invalid password,a appropriate errr message displayes.

    Returns:
        - If successful, it redirects to login page with a success message.
        - If there are errors in registration request, renders
          registration pagewith appropriate eror messages.
    """
    #  get name, email and password which are submitted by user
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    error_message = None

    # check if passwords do not match
    if password != confirm_password:
        error_message = 'La confirmation du mot de passe ne correspond pas. Merci de bien vouloir refaire une tentative.'

    # check if email is already is registered in the system
    elif is_email_exist(email):
        error_message = 'Cette adresse de courriel existe déja ! Merci de vien vous vérifier et de refaire une tentative.'

    # Check password complexity
    elif not is_valid_password(password):
        error_message = ('Password must be at least 12 characters long and contain at least '
                         '1 uppercase, 1 lowercase, 1 number, and 1 special character')

    # if there is an error in the registration request, return error message
    if error_message is not None:
        return render_template('register.html', error_message=error_message, email=email,
                               name=name)

    # if there is no any errors, Store user details in DB to complte the registration
    user_details = UserDetails(name=name, email=email, role='user')
    user_details.set_password(password)
    db.session.add(user_details)
    db.session.commit()

    # Redirect to login page with success message
    return redirect(url_for('login', registered=True))


@dbinstance.route('/orders')
# ‘/’ URL is bound with orders() function.
def orders():
    # check whether user is logged or not
    if 'user' in session:
        # if user has a active session get the username from the session
        name = session['user']['name']
        userId = session['user']['id']
        user_orders = fetch_orders_by_id(userId)
        return render_template('my-orders.html', username=name, orders=user_orders)
    # return login page to the user if user does not have an active session
    return redirect(url_for('login'))

'''
@dbinstance.route('/dossier')
# ‘/’ URL is bound with orders() function.
def dossier():
    # check whether user is logged or not
    if 'user' in session:
        # if user has a active session get the username from the session
        name = session['user']['name']
        userId = session['user']['id']
        user_dossiers = fetch_dossiers_by_id(userId)
        fv = flask.__version__
        pv = platform.python_version()
        return render_template('dossier.html', fv=fv, pv=pv, username=name, dossiers=user_dossiers)
    # return login page to the user if user does not have an active session
    return redirect(url_for('login'))
'''

@dbinstance.route('/password-update')
# ‘/’ URL is bound with password_update() function.
def password_update():
    """
    Render the password update page.

    If  user has n active session, the function get the username from the session.
    If the user is logged in, it renders the password update page. If there's a success message
    parameter in the URL, it's displayed to the user. If the user is not logged in, it redirects
    them to the login page with an error message.

    Returns:
        If the user is logged in, renders the password update page.
        If the user is not logged in, redirects to login page with an error message
    """

    # check whether user is logged or not
    if 'user' in session:
        success_msg = request.args.get('success_msg')  # get registered url parameter
        if success_msg:
            return render_template('password-update.html',
                                   username=session['user']['name'],
                                   success_message=success_msg)
        return render_template('password-update.html', username=session['user']['name'])

    # return login page to the user if user does not have an active session
    return redirect(url_for('login',
                            error_msg='you are required to log-in to perform password update'))


@dbinstance.route('/password-update', methods=['POST'])
def password_update_action():
    """
    Update password action
    """
    # Get new password which is submitted by the user
    new_password = request.form['password']

    error_message = None

    # Check password complexity
    if not is_valid_password(new_password):
        error_message = ('Password must be at least 12 characters long and contain at least'
                         ' 1 uppercase, 1 lowercase, 1 number, and 1 special character')

    email = session['user']['email']

    # Update the password in the db if there are no errors
    if error_message is None:
        # Retrieve the user from the database
        user = UserDetails.query.filter_by(email=email).first()

        if user:
            # Set the new password
            user.set_password(new_password)

            # Commit the changes to the database
            db.session.commit()

            # Redirect to password update page with success message
            return redirect(url_for('password_update', success_msg=
            'Your password has been successfully updated.'))

        else:
            error_message = 'User not found.'

    # If there are errors, render the template with the error message
    return render_template('password-update.html', error_message=error_message,
                           username=session['user']['name'])


@dbinstance.route('/logout')
# ‘/’ URL is bound with logout() function.
def logout():
    """
    Logout user.

    This function remove username from session, in roder to logging out the user.
    After removing the username from session, it redirect  user to  login page.

    Returns:
        Redirects to the login page after removing the username from the session.
    """
    # Remove the username from the session if it's there
    session.pop('user', None)
    # after remove username from sesion, redirect the user to login page
    return redirect(url_for('login'))


@dbinstance.route('/checkout')
# ‘/’ URL is bound with checkout() function.
def checkout():
    # check whether user is logged or not
    if 'user' in session:
        product_id = request.args.get('id')
        product = get_product_by_id(product_id)
        # if user has a active session get the username from the session
        username = session['user']['name']
        return render_template('checkout.html', username=username, product=product)
    # return login page to the user if user does not have an active session
    return redirect(url_for('login'))


@dbinstance.route('/pay', methods=["POST","GET"])
def pay():
    t_parceldem = get_all_parceldem()
    #t_parceldem = db.session.query(TParceldem).filter(TParceldem.par_nointerne.like("C22160001")).all()
    
    if request.method == 'POST':
        commune = cache.get("commune")
        section = cache.get("section")
        parcelles = cache.get("parcelles")
        form = Form()
        '''
        commune = db.session.query(TCom2023).filter_by(com=form.commune.data).first()
        cache.set("commune", db.session.query(TCom2023).filter_by(com=form.commune.data).first())
        section = db.session.query(TCadastre).filter_by(ccosec=form.section.data).first()
        cache.set("section", db.session.query(TCadastre).filter_by(ccosec=form.section.data).first())
        #parcelles = db.session.query(TCadastre.idsuf).where(and_((TCadastre.idcom==format(commune.com),(TCadastre.ccosec==format(section.ccosec))))).all()
        parcelles = db.session.query(TCadastre.idsuf).where(and_((TCadastre.idcom==commune.com),(TCadastre.ccosec==section.ccosec))).all()
        cache.set("parcelles", db.session.query(TCadastre.idsuf).where(and_((TCadastre.idcom==commune.com),(TCadastre.ccosec==section.ccosec))).all())
        '''
        form.commune.choices = [(commune.com, commune.libelle) for commune in db.session.query(TCom2023).filter_by(dep='22').all()]
            
        order_details = get_all_order_details()
        products = get_all_products()
        t_com2023 = get_all_t_com2023()
        #parcelles = get_all_parcelles()
        #com='search_com2023_id'
        #sections = fetch_sections_by_commune('22278')
   
        fv = flask.__version__
        pv = platform.python_version()
        # check whether user is logged or not
    
        # Get the order details from the form
        #user_id = session['user']['id']
        par_idsuf = request.form.get('parcelle_idsuf')
        #quantity = int(request.form.get('quantity'))
        #product = get_product_by_id(product_id)
        #parcelle = get_parcelle_by_idsuf(idsuf)
        #price = float(product.price)
        #total = price * quantity

        # Save the order details to the DB
        t_parceldem = TParceldem(par_idsuf=par_idsuf,
                                     par_nointerne="C22160001")

        db.session.add(t_parceldem)
        db.session.commit()
        #print(t_parceldem)
        #return redirect(url_for('dbinstance.home'))
        return render_template("index.html", t_parceldem=get_all_parceldem(), parcelles=parcelles, form=form, pv=pv, fv=fv, username=session[
        'user']['name'], order_details=order_details, products=products)  # return index.html with username of logged user


@dbinstance.route('/cancel-order', methods=['POST'])
def cancel_order():
    order_id = request.form.get('order_id')
    order = OrderDetails.query.get(order_id)

    if order:
        db.session.delete(order)
        db.session.commit()
        return redirect(url_for('orders'))

    return redirect(url_for('orders'))


# this method check if email already exists
def is_email_exist(email):
    """
    Check if email already exists in DB

    Args:
        email (str):  email address to check for existence in fil.

    Returns:
        bool: True if the email already exists,if not False .
    """
    existing_user = db.session.query(UserDetails).filter_by(email=email).first()
    return existing_user is not None


# this function validates password complexity
def is_valid_password(password):
    """
    Validate password complexity.

    This function checks whether the given password meet required complexity criteria:
    - At least 12 characters long
    - Contains at least 1 lowercase letter
    - Contains at least 1uppercase letter
    - Contains at least 1 digit
    - Contains at least 1 special character

    Args:
        password (str): The password to validate.

    Returns:
        bool: Trueif, the password meets the complexity criteria, False otherwise.
    """
    # validate length
    if len(password) < 12:
        return False
    # check for lowercase charactor
    if not re.search("[a-z]", password):
        return False
    # check for uppercase charactor
    if not re.search("[A-Z]", password):
        return False
    # check for a number
    if not re.search("[0-9]", password):
        return False
    # check for a special charactor
    if not re.search("[!@#$%^&*()_+=]", password):
        return False
    return True
    """
    Checks if email already exist in user_details.txt.

    Args:
        email (str):  email to check for existence.

    Returns:
        bool: True if the email already exists,not False.
    """
    with open('user_details.txt', 'r', encoding='utf-8') as user_details_file:
        for line in user_details_file:
            user, email_db, _ = line.strip().split(',')
            if email_db == email:
                return True
    return False


@dbinstance.route('/mailmerge')
# ‘/’ URL is bound with orders() function.

#def mailmerge(request):
def mailmerge():
        # check whether user is logged or not
    if 'user' in session:
        # if user has a active session get the username from the session
        name = session['user']['name']
        userId = session['user']['id']
        user_dossiers = fetch_dossiers_by_id(userId)
        fv = flask.__version__
        pv = platform.python_version()
    #sample = SampleList.objects.all()[0:15]
    #sample = TPub.query.all()[0:240]
    sample = db.session.query(TPub).all()[0:15]
    #sample = TPub.db.session.objects.all()[0:15]
    #sample = TPub.objects.all()[0:240]
    template = DocxTemplate("lab_management/word/sample_template.docx")

    context = {
        'headers' : ['SNAME', 'STYPE', 'HVER', 'SVER', 'CS', 'NUM', 'SNUM'],
        'list': [],
    }

    alist = ['a']

    for i in alist: 
        for samples in sample:
            '''content= [samples.sample_name, samples.sample_type, samples.hardware_version,
                      samples.software_version, samples.config_status, samples.number, 
                      samples.sample_number ]'''
            content= [samples.libelle_com, samples.libelle_paratel, samples.superficie,
                      samples.propoumandat, samples.adrpropoumandat, samples.demandeur, 
                      samples.adrdem, samples.cedant, samples.numdoss, samples.dateenreg,
                      samples.datelimit ]
            context['list'].append(content)

    #template.render(context)
    #template.save('lab_management/word/sample.docx')
    #return redirect('/lab/sample/details/')
    #response = Response(generate(), mimetype='text/docx')
    #response = Response(generate(), mimetype='application/msword')
    document = template
    #document = Document()
    #document.add_heading("Some head-title")
    #document.add_paragraph('Some text')
  
    #return send_file(f, mimetype='application/msword', as_attachment=True, download_name='output.doc') 
    #return Response(generate(), mimetype='text/docx')
    #response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    
    #response["Content-Disposition"] = 'filename="your_doc_name.docx"'
    document.render(context)
    #template.render(context)
    #template.save(response)
    f = BytesIO()
    document.save(f)
    f.seek(0)
    return send_file(f, as_attachment=True, download_name='your_doc_name.docx')    
    response = Response(send_file(), mimetype='application/msword')  
    
    return response
    return render_template('mailmerge.html', fv=fv, pv=pv, username=name, dossiers=user_dossiers)
    # return login page to the user if user does not have an active session
    return redirect(url_for('login'))
'''
with dbinstance.app_context():
    insert_default_products()
'''
if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=10000)
    app.run()
    
