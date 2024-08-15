from typing import List

from sqlalchemy import BigInteger, Boolean, Column, Date, Double, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class Products(Base):
    __tablename__ = 'products'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='products_pkey'),
    )

    id = mapped_column(Integer)
    name = mapped_column(String(128), nullable=False)
    price = mapped_column(Double(53), nullable=False)
    image_name = mapped_column(String(256), nullable=False)

    order_details: Mapped[List['OrderDetails']] = relationship('OrderDetails', uselist=True, back_populates='product')


class TDemande(Base):
    __tablename__ = 't_demande'
    __table_args__ = (
        PrimaryKeyConstraint('idt_demande', name='t_demande_pkey'),
    )

    idt_demande = mapped_column(BigInteger)
    no_interne = mapped_column(String(9), server_default=text('NULL::character varying'))
    date_de_depot = mapped_column(Date)
    date_complet = mapped_column(Date)
    code_avis = mapped_column(String(1), server_default=text('NULL::character varying'))
    id_commission = mapped_column(Integer)
    date_limiteval = mapped_column(Date)
    no_pacage_demandeur = mapped_column(String(9), server_default=text('NULL::character varying'))
    dem_autprof = mapped_column(String(30), server_default=text('NULL::character varying'))
    no_pacage_cedant = mapped_column(String(9), server_default=text('NULL::character varying'))
    jeune_agriculteur = mapped_column(Integer)
    jeune_agr_aide = mapped_column(Integer)
    code_motifcess = mapped_column(Integer)
    type_demande = mapped_column(Integer)
    cedantinforme = mapped_column(Integer)
    uta_demandeur = mapped_column(String(50), server_default=text('NULL::character varying'))
    nb_salaries = mapped_column(String(50), server_default=text('NULL::character varying'))
    sau_demandeur = mapped_column(String(50), server_default=text('NULL::character varying'))
    smi = mapped_column(String(2), server_default=text('NULL::character varying'))
    demanter = mapped_column(Integer)
    surface_demandee = mapped_column(String(50), server_default=text('NULL::character varying'))
    distance_siege = mapped_column(String(50), server_default=text('NULL::character varying'))
    distance_parcelle = mapped_column(String(50), server_default=text('NULL::character varying'))
    surface_unite_ref = mapped_column(String(50), server_default=text('NULL::character varying'))
    date_transfert = mapped_column(Date)
    demanhs = mapped_column(Integer)
    type_demande_hs = mapped_column(Integer)
    natu_demande_hs = mapped_column(Integer)
    effectifhs = mapped_column(Integer)
    sau_ponderee_demandeur = mapped_column(String(50), server_default=text('NULL::character varying'))
    pad_demandeur = mapped_column(String(50), server_default=text('NULL::character varying'))
    date_signature_decision = mapped_column(Date)
    motif_ctrl = mapped_column(String(2), server_default=text('NULL::character varying'))
    code_decision = mapped_column(String(1), server_default=text('NULL::character varying'))
    date_editdecis = mapped_column(Date)
    optimclecomp_no_pa_id_co = mapped_column(String(13), server_default=text('NULL::character varying'))
    sau_cedant = mapped_column(String(50), server_default=text('NULL::character varying'))
    date_avis = mapped_column(Date)
    code_statut = mapped_column(String(1), server_default=text('NULL::character varying'))
    motiv_c = mapped_column(Text)
    motiv_d = mapped_column(Text)
    motiv_a = mapped_column(Text)
    motiv_p = mapped_column(Text)
    sele_motictrl = mapped_column(Integer)
    id_commissioncode_statut = mapped_column(String(4), server_default=text('NULL::character varying'))
    no_pacage_demandeurid_commission = mapped_column(String(15), server_default=text('NULL::character varying'))
    no_pacage_cedantno_interne = mapped_column(String(20), server_default=text('NULL::character varying'))
    id_commissioncode_statutno_pacage_cedant = mapped_column(String(15), server_default=text('NULL::character varying'))
    aj6mois = mapped_column(String(1), server_default=text('NULL::character varying'))
    env_giee = mapped_column(Boolean)
    env_dephy = mapped_column(Boolean)
    env_cert_maaf = mapped_column(Boolean)
    env_cert_biopart = mapped_column(Boolean)
    env_cert_biotot = mapped_column(Boolean)
    distance_siege_proche = mapped_column(String(50), server_default=text('NULL::character varying'))
    distance_siege_eloigne = mapped_column(String(50), server_default=text('NULL::character varying'))
    rt_compens_utilpub = mapped_column(Boolean)
    rt_compens_utilpub_surf = mapped_column(String(50), server_default=text('NULL::character varying'))
    rt_compens_rprop = mapped_column(Boolean)
    rt_compens_rprop_surf = mapped_column(Integer)
    rt_compens_autre = mapped_column(Boolean)
    rt_compens_autre_surf = mapped_column(String(50), server_default=text('NULL::character varying'))
    rt_compens_autre_motif = mapped_column(String(50), server_default=text('NULL::character varying'))
    rt_deplanimaux = mapped_column(Boolean)
    rt_deplanimaux_surf = mapped_column(String(50), server_default=text('NULL::character varying'))
    rt_echcedant = mapped_column(Boolean)
    rt_echcedant_surf = mapped_column(String(50), server_default=text('NULL::character varying'))
    rt_bio = mapped_column(Boolean)
    rt_bio_surf = mapped_column(String(50), server_default=text('NULL::character varying'))
    surf_rep_bio = mapped_column(String(50), server_default=text('NULL::character varying'))
    surf_rep_echange = mapped_column(String(50), server_default=text('NULL::character varying'))
    surf_rep_depanimaux = mapped_column(Integer)
    reprise_dossier = mapped_column(Boolean)
    date_limite_depot = mapped_column(Date)
    nb_concurrences = mapped_column(Integer)
    env_titre_sec = mapped_column(Boolean)
    id_naturetransac = mapped_column(Integer)
    instal3p = mapped_column(Integer)
    instalstage = mapped_column(Integer)
    instaletude = mapped_column(Integer)
    cedantexpab = mapped_column(Integer)
    cedantexpconv = mapped_column(Integer)
    rt_compens_ind_surf = mapped_column(Boolean)
    ide_globale = mapped_column(String(50), server_default=text('NULL::character varying'))
    surf_zsce = mapped_column(String(50), server_default=text('NULL::character varying'))
    id_redaction_decision = mapped_column(Integer)
    total_ide = mapped_column(String(50), server_default=text('NULL::character varying'))
    id_gestionnaire = mapped_column(Integer)
    demandebat = mapped_column(Integer)
    saup = mapped_column(String(50), server_default=text('NULL::character varying'))
    dossiersuccessif = mapped_column(Boolean)
    dossierconcurrentsuccessif = mapped_column(Boolean)
    ideuta = mapped_column(String(50), server_default=text('NULL::character varying'))
    memodemandeur = mapped_column(Text)
    memocedant = mapped_column(Text)
    recours = mapped_column(Boolean)
    daterecours = mapped_column(Date)
    id_logics = mapped_column(String(50), server_default=text('NULL::character varying'))
    pideuta = mapped_column(String(50), server_default=text('NULL::character varying'))
    schema = mapped_column(Integer)
    sempastous = mapped_column(Boolean)
    date_sempastous = mapped_column(Date)


class UserDetails(Base):
    __tablename__ = 'user_details'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='user_details_pkey'),
        UniqueConstraint('email', name='user_details_email_key')
    )

    id = mapped_column(Integer)
    name = mapped_column(String(128), nullable=False)
    email = mapped_column(String(128), nullable=False)
    password = mapped_column(String(128), nullable=False)
    role = mapped_column(String(64), nullable=False)

    order_details: Mapped[List['OrderDetails']] = relationship('OrderDetails', uselist=True, back_populates='user_details')


class OrderDetails(Base):
    __tablename__ = 'order_details'
    __table_args__ = (
        ForeignKeyConstraint(['product_id'], ['products.id'], name='order_details_product_id_fkey'),
        ForeignKeyConstraint(['username'], ['user_details.id'], name='order_details_username_fkey'),
        PrimaryKeyConstraint('id', name='order_details_pkey')
    )

    id = mapped_column(Integer)
    username = mapped_column(Integer, nullable=False)
    product_id = mapped_column(Integer, nullable=False)
    delivery_address = mapped_column(String(256), nullable=False)
    product_name = mapped_column(String(128), nullable=False)
    quantity = mapped_column(Integer, nullable=False)
    price = mapped_column(Double(53), nullable=False)
    total = mapped_column(Double(53), nullable=False)

    product: Mapped['Products'] = relationship('Products', back_populates='order_details')
    user_details: Mapped['UserDetails'] = relationship('UserDetails', back_populates='order_details')
