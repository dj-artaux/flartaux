from db_init import db
import bcrypt

import os

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Text, Date, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.inspection import inspect
from sqlalchemy.dialects import postgresql

Base = declarative_base()
#from sqlalchemy.orm import Column
from sqlalchemy import create_engine, Column, Integer, BigInteger, Text, Date, Boolean, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base

# Define Table Classes
Base = declarative_base()

class TCom2023(db.Model):
    __tablename__ = 't_com2023'

    idt_com2023 = Column(BigInteger, primary_key=True, autoincrement=True)
    com = Column(String(5))
    dep = Column(String(3))
    can = Column(String(5))
    libelle = Column(String(255))

class TCadastre(db.Model):
    __tablename__ = 't_cadastre'

    idt_cadastre = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    idsuf = db.Column(db.String(16))
    idpar = db.Column(db.String(16))
    idprocpte = db.Column(db.String(16))
    idcom = db.Column(db.String(5))
    ccosec = db.Column(db.String(2))
    dnupla = db.Column(db.String(4))
    ccosub = db.Column(db.String(2))
    dcntsf = db.Column(db.BigInteger)
    idprocpte_org = db.Column(db.Text)

class TPub(Base):
    __tablename__ = 't_pub'
#    __table_args__ = (
#        PrimaryKeyConstraint('idt_pub', name='t_pub_pkey'),
#    )

    #idt_pub = Column(BigInteger)
    idt_pub = Column(BigInteger, primary_key=True)
    libelle_com = Column(Text)
    libelle_paratel = Column(Text)
    superficie = Column(String(12))
    propoumandat = Column(Text)
    adrpropoumandat = Column(Text)
    demandeur = Column(Text)
    adrdem = Column(Text)
    cedant = Column(Text)
    numdoss = Column(String(9))
    dateenreg = Column(Text)
    datelimit = Column(Text)


class TUsager(Base):
    __tablename__ = 't_usager'
    #__table_args__ = (
    #    PrimaryKeyConstraint('idt_usager', name='t_usager_pkey'),
    #)
    idt_usager = Column(BigInteger, primary_key=True)
    #idt_usager = Column(BigInteger)
    u_pacage = Column(String(9))
    u_civilite = Column(String(12))
    u_nom_raison_sociale = Column(String(40))
    u_prenoms = Column(String(30))
    u_forme_juridique = Column(String(50))
    u_siret = Column(String(14))
    u_msa = Column(String(14))
    u_etat = Column(String(10))
    u_date_debut_validite_sigc = Column(String(10))
    u_date_fin_validite_sigc = Column(String(10))
    u_date_cloture = Column(String(10))
    u_civilite_edit = Column(String(30))


class TDemande(db.Model):
    __tablename__ = 't_demande'
    idt_demande = Column(BigInteger, primary_key=True)
    #country = Column(String)
    #idt_demande = Column(BigInteger)
    no_interne = Column(String(9))
    date_de_depot = Column(Date)
    date_complet = Column(Date)
    code_avis = Column(String(1))
    id_commission = Column(Integer)
    date_limiteval = Column(Date)
    no_pacage_demandeur = Column(String(9))
    dem_autprof = Column(String(30))
    no_pacage_cedant = Column(String(9))
    jeune_agriculteur = Column(Integer)
    jeune_agr_aide = Column(Integer)
    code_motifcess = Column(Integer)
    type_demande = Column(Integer)
    cedantinforme = Column(Integer)
    uta_demandeur = Column(String(50))
    nb_salaries = Column(String(50))
    sau_demandeur = Column(String(50))
    smi = Column(String(2))
    demanter = Column(Integer)
    surface_demandee = Column(String(50))
    distance_siege = Column(String(50))
    distance_parcelle = Column(String(50))
    surface_unite_ref = Column(String(50))
    date_transfert = Column(Date)
    demanhs = Column(Integer)
    type_demande_hs = Column(Integer)
    natu_demande_hs = Column(Integer)
    effectifhs = Column(Integer)
    sau_ponderee_demandeur = Column(String(50))
    pad_demandeur = Column(String(50))
    date_signature_decision = Column(Date)
    motif_ctrl = Column(String(2))
    code_decision = Column(String(1))
    date_editdecis = Column(Date)
    optimclecomp_no_pa_id_co = Column(String(13))
    sau_cedant = Column(String(50))
    date_avis = Column(Date)
    code_statut = Column(String(1))
    motiv_c = Column(Text)
    motiv_d = Column(Text)
    motiv_a = Column(Text)
    motiv_p = Column(Text)
    sele_motictrl = Column(Integer)
    id_commissioncode_statut = Column(String(4))
    no_pacage_demandeurid_commission = Column(String(15))
    no_pacage_cedantno_interne = Column(String(20))
    id_commissioncode_statutno_pacage_cedant = Column(String(15))
    aj6mois = Column(String(1))
    env_giee = Column(Boolean)
    env_dephy = Column(Boolean)
    env_cert_maaf = Column(Boolean)
    env_cert_biopart = Column(Boolean)
    env_cert_biotot = Column(Boolean)
    distance_siege_proche = Column(String(50))
    distance_siege_eloigne = Column(String(50))
    rt_compens_utilpub = Column(Boolean)
    rt_compens_utilpub_surf = Column(String(50))
    rt_compens_rprop = Column(Boolean)
    rt_compens_rprop_surf = Column(Integer)
    rt_compens_autre = Column(Boolean)
    rt_compens_autre_surf = Column(String(50))
    rt_compens_autre_motif = Column(String(50))
    rt_deplanimaux = Column(Boolean)
    rt_deplanimaux_surf = Column(String(50))
    rt_echcedant = Column(Boolean)
    rt_echcedant_surf = Column(String(50))
    rt_bio = Column(Boolean)
    rt_bio_surf = Column(String(50))
    surf_rep_bio = Column(String(50))
    surf_rep_echange = Column(String(50))
    surf_rep_depanimaux = Column(Integer)
    reprise_dossier = Column(Boolean)
    date_limite_depot = Column(Date)
    nb_concurrences = Column(Integer)
    env_titre_sec = Column(Boolean)
    id_naturetransac = Column(Integer)
    instal3p = Column(Integer)
    instalstage = Column(Integer)
    instaletude = Column(Integer)
    cedantexpab = Column(Integer)
    cedantexpconv = Column(Integer)
    rt_compens_ind_surf = Column(Boolean)
    ide_globale = Column(String(50))
    surf_zsce = Column(String(50))
    id_redaction_decision = Column(Integer)
    total_ide = Column(String(50))
    id_gestionnaire = Column(Integer)
    demandebat = Column(Integer)
    saup = Column(String(50))
    dossiersuccessif = Column(Boolean)
    dossierconcurrentsuccessif = Column(Boolean)
    ideuta = Column(String(50))
    memodemandeur = Column(Text)
    memocedant = Column(Text)
    recours = Column(Boolean)
    daterecours = Column(Date)
    id_logics = Column(String(50))
    pideuta = Column(String(50))
    schema = Column(Integer)
    sempastous = Column(Boolean)
    date_sempastous = Column(Date)
    user_id = Column(Integer)

class Country(db.Model):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    country = Column(String)
    # Child
    cities = relationship("City", back_populates="country")


class City(db.Model):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    city = Column(String)
    # Parent
    country_id = Column(Integer, ForeignKey("country.id"))
    country = relationship("Country", back_populates="cities")


class Customer(db.Model):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    customer = Column(String)



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


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_name = db.Column(db.String(256), nullable=False)

    def __init__(self, id, name, price, image_name):
        self.id = id
        self.name = name
        self.price = price
        self.image_name = image_name


class OrderDetails(db.Model):
    __tablename__ = 'order_details'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Integer, db.ForeignKey('user_details.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    delivery_address = db.Column(db.String(256), nullable=False)
    product_name = db.Column(db.String(128), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)

    def __init__(self, username, product_id, delivery_address, product_name, quantity, price, total):
        self.username = username
        self.product_id = product_id
        self.delivery_address = delivery_address
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.total = total



class TParceldem(db.Model):    
    __tablename__ = 't_parceldem'
    idt_parceldem = Column(BigInteger, primary_key=True)
    par_nointerne = Column(String(9))
    par_insee = Column(BigInteger)
    par_idsuf = Column(String(16))
    par_section = Column(String(2))
    par_parcelle = Column(BigInteger)
    par_subdi = Column(String(2))
    par_surface = Column(String(10))
    par_idpropr = Column(String(11))
    par_insecpasu = Column(String(22))
    par_ok = Column(Boolean)
    par_bio = Column(Boolean)
    par_echange = Column(Boolean)
    par_deplanimaux = Column(Boolean)
    par_nointernepar_idproprpar_insee = Column(String(29))
    par_nointernepar_idpropr = Column(String(23))
    par_nointernepar_insee = Column(Text)
    par_est_modif = Column(Boolean)
    par_nointernepar_idsuf = Column(Text)
    par_dist_siege = Column(String(10))
    par_surf5 = Column(String(10))
    par_sur5a10 = Column(String(10))
    par_surf10 = Column(String(10))
    par_type_surf = Column(Boolean)
    par_vol = Column(String(10))
    par_cal = Column(String(10))
    par_export = Column(Boolean)
    par_prox = Column(Boolean)
    par_liaison = Column(Boolean)
    parc_enclave = Column(Boolean)
    par_export_sig = Column(Boolean)
    parc_zsce = Column(Boolean)
    par_volsiege = Column(String(10))

