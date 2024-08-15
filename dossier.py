import sys
import platform
import flask
import re
import logging
import os

from database import db
from flask import render_template
from flask.blueprints import Blueprint
from flask import current_app
from flask import Flask, session
from flask import request, flash

dbinstance = Blueprint('dbinstance', __name__,
                 template_folder='templates',
                 static_folder='static')
                 
from model import Base
import bcrypt

import os

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.inspection import inspect
from sqlalchemy.dialects import postgresql
#from sqlalchemy import db.db.db.mapped_column, Table, Column, Bigdb.Integer, db.Integer, db.db.Text, db.Date, db.Boolean, db.db.db.String, ForeignKey
from sqlalchemy import desc


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
        return render_template('dossier.html', fv=fv, pv=pv, username=session[
            'user']['name'], dossiers=user_dossiers)
    # return login page to the user if user does not have an active session
    return redirect(url_for('login'))


@dbinstance.route('/getdossier', methods=['GET', 'POST'])
def getdossier():

    dossiers = get_dossier()
    if request.method == 'POST' :
        username=session['user']['name']
        user_id = session['user']['id']
        no_interne = request.form.get('no_interne')
        product_name = request.form.get('product_name')
        no_interne = fetch_dossiers_by_no_interne(no_interne)

        fv = flask.__version__
        pv = platform.python_version()
        return render_template('dossier.html', fv=fv, pv=pv, dossiers=no_interne, username=username, user_id=user_id)

        db.session.commit()

    return redirect(url_for('dossier'))
    
def fetch_dossiers_by_no_interne(no_interne):

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

def get_dossier():
    if 'user' in session:
        user_id = session['user']['id']
        no_interne = request.form.get('no_interne')

        flash('test :' , str(no_interne))
        print('order_id:', str(no_interne))
        return db.session.query(TDemande).where(TDemande.no_interne == str(no_interne))
    return db.session.query(TDemande).where(TDemande.no_interne == str(no_interne))    

class TUsager(db.Model):
    __tablename__ = 't_usager'
    idt_usager = db.Column(db.BigInteger, primary_key=True)
    u_pacage = db.mapped_column(db.String(9))
    u_civilite = db.mapped_column(db.String(12))
    u_nom_raison_sociale = db.mapped_column(db.String(40))
    u_prenoms = db.mapped_column(db.String(30))
    u_forme_juridique = db.mapped_column(db.String(50))
    u_siret = db.mapped_column(db.String(14))
    u_msa = db.mapped_column(db.String(14))
    u_etat = db.mapped_column(db.String(10))
    u_date_debut_validite_sigc = db.mapped_column(db.String(10))
    u_date_fin_validite_sigc = db.mapped_column(db.String(10))
    u_date_cloture = db.mapped_column(db.String(10))
    u_civilite_edit = db.mapped_column(db.String(30))
    
class TDemande(db.Model):

    __tablename__ = 't_demande'
    idt_demande = db.Column(db.BigInteger, primary_key=True)
    no_interne = db.mapped_column(db.String(9))
    date_de_depot = db.mapped_column(db.Date)
    date_complet = db.mapped_column(db.Date)
    code_avis = db.mapped_column(db.String(1))
    id_commission = db.mapped_column(db.Integer)
    date_limiteval = db.mapped_column(db.Date)
    no_pacage_demandeur = db.mapped_column(db.String(9))
    dem_autprof = db.mapped_column(db.String(30))
    no_pacage_cedant = db.mapped_column(db.String(9))
    jeune_agriculteur = db.mapped_column(db.Integer)
    jeune_agr_aide = db.mapped_column(db.Integer)
    code_motifcess = db.mapped_column(db.Integer)
    type_demande = db.mapped_column(db.Integer)
    cedantinforme = db.mapped_column(db.Integer)
    uta_demandeur = db.mapped_column(db.String(50))
    nb_salaries = db.mapped_column(db.String(50))
    sau_demandeur = db.mapped_column(db.String(50))
    smi = db.mapped_column(db.String(2))
    demanter = db.mapped_column(db.Integer)
    surface_demandee = db.mapped_column(db.String(50))
    distance_siege = db.mapped_column(db.String(50))
    distance_parcelle = db.mapped_column(db.String(50))
    surface_unite_ref = db.mapped_column(db.String(50))
    date_transfert = db.mapped_column(db.Date)
    demanhs = db.mapped_column(db.Integer)
    type_demande_hs = db.mapped_column(db.Integer)
    natu_demande_hs = db.mapped_column(db.Integer)
    effectifhs = db.mapped_column(db.Integer)
    sau_ponderee_demandeur = db.mapped_column(db.String(50))
    pad_demandeur = db.mapped_column(db.String(50))
    date_signature_decision = db.mapped_column(db.Date)
    motif_ctrl = db.mapped_column(db.String(2))
    code_decision = db.mapped_column(db.String(1))
    date_editdecis = db.mapped_column(db.Date)
    optimclecomp_no_pa_id_co = db.mapped_column(db.String(13))
    sau_cedant = db.mapped_column(db.String(50))
    date_avis = db.mapped_column(db.Date)
    code_statut = db.mapped_column(db.String(1))
    motiv_c = db.mapped_column(db.Text)
    motiv_d = db.mapped_column(db.Text)
    motiv_a = db.mapped_column(db.Text)
    motiv_p = db.mapped_column(db.Text)
    sele_motictrl = db.mapped_column(db.Integer)
    id_commissioncode_statut = db.mapped_column(db.String(4))
    no_pacage_demandeurid_commission = db.mapped_column(db.String(15))
    no_pacage_cedantno_interne = db.mapped_column(db.String(20))
    id_commissioncode_statutno_pacage_cedant = db.mapped_column(db.String(15))
    aj6mois = db.mapped_column(db.String(1))
    env_giee = db.mapped_column(db.Boolean)
    env_dephy = db.mapped_column(db.Boolean)
    env_cert_maaf = db.mapped_column(db.Boolean)
    env_cert_biopart = db.mapped_column(db.Boolean)
    env_cert_biotot = db.mapped_column(db.Boolean)
    distance_siege_proche = db.mapped_column(db.String(50))
    distance_siege_eloigne = db.mapped_column(db.String(50))
    rt_compens_utilpub = db.mapped_column(db.Boolean)
    rt_compens_utilpub_surf = db.mapped_column(db.String(50))
    rt_compens_rprop = db.mapped_column(db.Boolean)
    rt_compens_rprop_surf = db.mapped_column(db.Integer)
    rt_compens_autre = db.mapped_column(db.Boolean)
    rt_compens_autre_surf = db.mapped_column(db.String(50))
    rt_compens_autre_motif = db.mapped_column(db.String(50))
    rt_deplanimaux = db.mapped_column(db.Boolean)
    rt_deplanimaux_surf = db.mapped_column(db.String(50))
    rt_echcedant = db.mapped_column(db.Boolean)
    rt_echcedant_surf = db.mapped_column(db.String(50))
    rt_bio = db.mapped_column(db.Boolean)
    rt_bio_surf = db.mapped_column(db.String(50))
    surf_rep_bio = db.mapped_column(db.String(50))
    surf_rep_echange = db.mapped_column(db.String(50))
    surf_rep_depanimaux = db.mapped_column(db.Integer)
    reprise_dossier = db.mapped_column(db.Boolean)
    date_limite_depot = db.mapped_column(db.Date)
    nb_concurrences = db.mapped_column(db.Integer)
    env_titre_sec = db.mapped_column(db.Boolean)
    id_naturetransac = db.mapped_column(db.Integer)
    instal3p = db.mapped_column(db.Integer)
    instalstage = db.mapped_column(db.Integer)
    instaletude = db.mapped_column(db.Integer)
    cedantexpab = db.mapped_column(db.Integer)
    cedantexpconv = db.mapped_column(db.Integer)
    rt_compens_ind_surf = db.mapped_column(db.Boolean)
    ide_globale = db.mapped_column(db.String(50))
    surf_zsce = db.mapped_column(db.String(50))
    id_redaction_decision = db.mapped_column(db.Integer)
    total_ide = db.mapped_column(db.String(50))
    id_gestionnaire = db.mapped_column(db.Integer)
    demandebat = db.mapped_column(db.Integer)
    saup = db.mapped_column(db.String(50))
    dossiersuccessif = db.mapped_column(db.Boolean)
    dossierconcurrentsuccessif = db.mapped_column(db.Boolean)
    ideuta = db.mapped_column(db.String(50))
    memodemandeur = db.mapped_column(db.Text)
    memocedant = db.mapped_column(db.Text)
    recours = db.mapped_column(db.Boolean)
    daterecours = db.mapped_column(db.Date)
    id_logics = db.mapped_column(db.String(50))
    pideuta = db.mapped_column(db.String(50))
    schema = db.mapped_column(db.Integer)
    sempastous = db.mapped_column(db.Boolean)
    date_sempastous = db.mapped_column(db.Date)
    user_id = db.mapped_column(db.Integer)
