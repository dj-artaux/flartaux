from typing import List, Optional

from sqlalchemy import BigInteger, Boolean, Column, Date, Double, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class Country(Base):
    __tablename__ = 'country'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='country_pkey'),
    )

    id = mapped_column(Integer)
    country = mapped_column(String)

    city: Mapped[List['City']] = relationship('City', uselist=True, back_populates='country')


class Customer(Base):
    __tablename__ = 'customer'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='customer_pkey'),
    )

    id = mapped_column(Integer)
    customer = mapped_column(String)


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


class TCadastre(Base):
    __tablename__ = 't_cadastre'
    __table_args__ = (
        PrimaryKeyConstraint('idt_cadastre', name='t_cadastre_pkey'),
    )

    idt_cadastre = mapped_column(BigInteger)
    idsuf = mapped_column(String(16), server_default=text('NULL::character varying'))
    idpar = mapped_column(String(16), server_default=text('NULL::character varying'))
    idprocpte = mapped_column(String(16), server_default=text('NULL::character varying'))
    idcom = mapped_column(String(5), server_default=text('NULL::character varying'))
    ccosec = mapped_column(String(2), server_default=text('NULL::character varying'))
    dnupla = mapped_column(String(4), server_default=text('NULL::character varying'))
    ccosub = mapped_column(String(2), server_default=text('NULL::character varying'))
    dcntsf = mapped_column(BigInteger)
    idprocpte_org = mapped_column(Text)


class TCom2023(Base):
    __tablename__ = 't_com2023'
    __table_args__ = (
        PrimaryKeyConstraint('idt_com2023', name='t_com2023_pkey'),
    )

    idt_com2023 = mapped_column(BigInteger)
    com = mapped_column(String(5), server_default=text('NULL::character varying'))
    dep = mapped_column(String(3), server_default=text('NULL::character varying'))
    can = mapped_column(String(5), server_default=text('NULL::character varying'))
    libelle = mapped_column(String(255), server_default=text('NULL::character varying'))


class TCommune(Base):
    __tablename__ = 't_commune'
    __table_args__ = (
        PrimaryKeyConstraint('idt_commune', name='t_commune_pkey'),
    )

    idt_commune = mapped_column(BigInteger)
    code_insee_commune = mapped_column(String(5), server_default=text('NULL::character varying'))
    code_dep = mapped_column(String(3), server_default=text('NULL::character varying'))
    code_canton = mapped_column(String(4), server_default=text('NULL::character varying'))
    libelle_commune = mapped_column(String(74), server_default=text('NULL::character varying'))


class TCommuneComobs(Base):
    __tablename__ = 't_commune_comobs'
    __table_args__ = (
        PrimaryKeyConstraint('idt_commune_comobs', name='t_commune_comobs_pkey'),
    )

    idt_commune_comobs = mapped_column(BigInteger)
    code_insee_commune = mapped_column(String(5), server_default=text('NULL::character varying'))
    code_dep = mapped_column(String(3), server_default=text('NULL::character varying'))
    code_canton = mapped_column(String(4), server_default=text('NULL::character varying'))
    libelle_commune = mapped_column(String(255), server_default=text('NULL::character varying'))
    comobs = mapped_column(Boolean)


class TDateCommission(Base):
    __tablename__ = 't_date_commission'
    __table_args__ = (
        PrimaryKeyConstraint('idt_date_commission', name='t_date_commission_pkey'),
    )

    idt_date_commission = mapped_column(BigInteger)
    id_commission = mapped_column(BigInteger)
    date_commission = mapped_column(Date)


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
    user_id = mapped_column(Integer)


class TDemandeBatiment(Base):
    __tablename__ = 't_demande_batiment'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='t_demande_batiment_pkey'),
    )

    id = mapped_column(BigInteger)
    idt_demande_batiment = mapped_column(BigInteger)
    id_interne = mapped_column(String(9), server_default=text('NULL::character varying'))
    id_atelier = mapped_column(BigInteger)
    nb_atelier = mapped_column(String(20), server_default=text('NULL::character varying'))
    code_insee = mapped_column(String(5), server_default=text('NULL::character varying'))
    unite = mapped_column(BigInteger)
    indiceatelier = mapped_column(BigInteger)
    idsuf = mapped_column(String(17), server_default=text('NULL::character varying'))


class TMvtcommune(Base):
    __tablename__ = 't_mvtcommune'
    __table_args__ = (
        PrimaryKeyConstraint('idt_mvtcommune', name='t_mvtcommune_pkey'),
    )

    idt_mvtcommune = mapped_column(BigInteger)
    mod = mapped_column(Integer)
    dateeff = mapped_column(Date)
    typecomav = mapped_column(String(4), server_default=text('NULL::character varying'))
    comav = mapped_column(String(5), server_default=text('NULL::character varying'))
    tnccav = mapped_column(Integer)
    nccav = mapped_column(String(255), server_default=text('NULL::character varying'))
    nccenrav = mapped_column(String(255), server_default=text('NULL::character varying'))
    libelleav = mapped_column(String(255), server_default=text('NULL::character varying'))
    typecomap = mapped_column(String(4), server_default=text('NULL::character varying'))
    comap = mapped_column(String(5), server_default=text('NULL::character varying'))
    tnccap = mapped_column(Integer)
    nccap = mapped_column(String(255), server_default=text('NULL::character varying'))
    nccenrap = mapped_column(String(255), server_default=text('NULL::character varying'))
    libelleap = mapped_column(String(255), server_default=text('NULL::character varying'))


class TParcelStatut(Base):
    __tablename__ = 't_parcel_statut'
    __table_args__ = (
        PrimaryKeyConstraint('idt_parcel_statut', name='t_parcel_statut_pkey'),
    )

    idt_parcel_statut = mapped_column(BigInteger)
    id_parcel_statut = mapped_column(String(17), server_default=text('NULL::character varying'))
    par_idsuf = mapped_column(String(17), server_default=text('NULL::character varying'))
    no_interne = mapped_column(String(9), server_default=text('NULL::character varying'))
    no_interne_pub = mapped_column(String(9), server_default=text('NULL::character varying'))
    date_pub_pref = mapped_column(Date)
    date_pub_mairie = mapped_column(Date)
    date_limite_concu = mapped_column(Date)
    par_idsufno_interne = mapped_column(String(255), server_default=text('NULL::character varying'))
    par_idsufno_interne_pub = mapped_column(String(255), server_default=text('NULL::character varying'))


class TParceldem(Base):
    __tablename__ = 't_parceldem'
    __table_args__ = (
        PrimaryKeyConstraint('idt_parceldem', name='t_parceldem_pkey'),
    )

    idt_parceldem = mapped_column(BigInteger)
    par_nointerne = mapped_column(String(9), server_default=text('NULL::character varying'))
    par_insee = mapped_column(BigInteger)
    par_idsuf = mapped_column(String(16), server_default=text('NULL::character varying'))
    par_section = mapped_column(String(2), server_default=text('NULL::character varying'))
    par_parcelle = mapped_column(BigInteger)
    par_subdi = mapped_column(String(2), server_default=text('NULL::character varying'))
    par_surface = mapped_column(String(10), server_default=text('NULL::character varying'))
    par_idpropr = mapped_column(String(11), server_default=text('NULL::character varying'))
    par_insecpasu = mapped_column(String(22), server_default=text('NULL::character varying'))
    par_ok = mapped_column(Boolean, server_default=text('false'))
    par_bio = mapped_column(Boolean, server_default=text('false'))
    par_echange = mapped_column(Boolean, server_default=text('false'))
    par_deplanimaux = mapped_column(Boolean, server_default=text('false'))
    par_nointernepar_idproprpar_insee = mapped_column(String(29), server_default=text('NULL::character varying'))
    par_nointernepar_idpropr = mapped_column(String(23), server_default=text('NULL::character varying'))
    par_nointernepar_insee = mapped_column(Text)
    par_est_modif = mapped_column(Boolean, server_default=text('true'))
    par_nointernepar_idsuf = mapped_column(Text)
    par_dist_siege = mapped_column(String(10), server_default=text('NULL::character varying'))
    par_surf5 = mapped_column(String(10), server_default=text('NULL::character varying'))
    par_sur5a10 = mapped_column(String(10), server_default=text('NULL::character varying'))
    par_surf10 = mapped_column(String(10), server_default=text('NULL::character varying'))
    par_type_surf = mapped_column(Boolean, server_default=text('false'))
    par_vol = mapped_column(String(10), server_default=text('NULL::character varying'))
    par_cal = mapped_column(String(10), server_default=text('NULL::character varying'))
    par_export = mapped_column(Boolean, server_default=text('false'))
    par_prox = mapped_column(Boolean, server_default=text('false'))
    par_liaison = mapped_column(Boolean, server_default=text('false'))
    parc_enclave = mapped_column(Boolean, server_default=text('false'))
    par_export_sig = mapped_column(Boolean, server_default=text('false'))
    parc_zsce = mapped_column(Boolean, server_default=text('false'))
    par_volsiege = mapped_column(String(10), server_default=text('NULL::character varying'))


class TPropriDemand(Base):
    __tablename__ = 't_propri_demand'
    __table_args__ = (
        PrimaryKeyConstraint('idt_propri_demand', name='t_propri_demand_pkey'),
    )

    idt_propri_demand = mapped_column(BigInteger)
    pro_nointerne = mapped_column(String(9), server_default=text('NULL::character varying'))
    pro_ident = mapped_column(String(13), server_default=text('NULL::character varying'))
    pro_idcpte = mapped_column(String(11), server_default=text('NULL::character varying'))
    pro_commune = mapped_column(String(5), server_default=text('NULL::character varying'))
    pro_nointernepro_ident = mapped_column(String(23), server_default=text('NULL::character varying'))
    pro_informer = mapped_column(Boolean)
    pro_est_modif = mapped_column(Boolean)


class TPropriExclus(Base):
    __tablename__ = 't_propri_exclus'
    __table_args__ = (
        PrimaryKeyConstraint('idt_propri_exclus', name='t_propri_exclus_pkey'),
    )

    idt_propri_exclus = mapped_column(BigInteger)
    idprodroit = mapped_column(String(13), server_default=text('NULL::character varying'))
    idsuf = mapped_column(String(16), server_default=text('NULL::character varying'))
    no_interne = mapped_column(String(9), server_default=text('NULL::character varying'))
    idprodroitidsuf = mapped_column(String(30), server_default=text('NULL::character varying'))


class TProprietaires(Base):
    __tablename__ = 't_proprietaires'
    __table_args__ = (
        PrimaryKeyConstraint('idt_proprietaires', name='t_proprietaires_pkey'),
    )

    idt_proprietaires = mapped_column(BigInteger)
    idprodroit = mapped_column(String(13), server_default=text('NULL::character varying'))
    idprocpte = mapped_column(String(11), server_default=text('NULL::character varying'))
    idcom = mapped_column(String(9), server_default=text('NULL::character varying'))
    dnulp = mapped_column(String(9), server_default=text('NULL::character varying'))
    dnuper = mapped_column(String(9), server_default=text('NULL::character varying'))
    dforme = mapped_column(String(9), server_default=text('NULL::character varying'))
    ddenom = mapped_column(String(60), server_default=text('NULL::character varying'))
    dlign3 = mapped_column(String(30), server_default=text('NULL::character varying'))
    dlign4 = mapped_column(String(36), server_default=text('NULL::character varying'))
    dlign5 = mapped_column(String(30), server_default=text('NULL::character varying'))
    dlign6 = mapped_column(String(32), server_default=text('NULL::character varying'))
    ccodro = mapped_column(String(9), server_default=text('NULL::character varying'))
    modif = mapped_column(Boolean)
    suppr = mapped_column(Boolean)
    ajout = mapped_column(Boolean)
    civilite = mapped_column(String(30), server_default=text('NULL::character varying'))
    clef = mapped_column(String(25), server_default=text('NULL::character varying'))


class TPub(Base):
    __tablename__ = 't_pub'
    __table_args__ = (
        PrimaryKeyConstraint('idt_pub', name='t_pub_pkey'),
    )

    idt_pub = mapped_column(BigInteger)
    libelle_com = mapped_column(Text)
    libelle_paratel = mapped_column(Text)
    superficie = mapped_column(String(12), server_default=text('NULL::character varying'))
    propoumandat = mapped_column(Text)
    adrpropoumandat = mapped_column(Text)
    demandeur = mapped_column(Text)
    adrdem = mapped_column(Text)
    cedant = mapped_column(Text)
    numdoss = mapped_column(String(9), server_default=text('NULL::character varying'))
    dateenreg = mapped_column(Text)
    datelimit = mapped_column(Text)


class TTypeAtelier(Base):
    __tablename__ = 't_type_atelier'
    __table_args__ = (
        PrimaryKeyConstraint('idt_type_atelier', name='t_type_atelier_pkey'),
    )

    id = mapped_column(BigInteger, nullable=False)
    idt_type_atelier = mapped_column(BigInteger)
    lib_atelier = mapped_column(String(100), server_default=text('NULL::character varying'))


class TUnite(Base):
    __tablename__ = 't_unite'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='t_unite_pkey'),
    )

    id = mapped_column(BigInteger)
    idt_unite = mapped_column(BigInteger)
    libunite = mapped_column(String(100), server_default=text('NULL::character varying'))


class TUsadresse(Base):
    __tablename__ = 't_usadresse'
    __table_args__ = (
        PrimaryKeyConstraint('idt_usadresse', name='t_usadresse_pkey'),
    )

    idt_usadresse = mapped_column(BigInteger)
    adr_pacage = mapped_column(String(9), server_default=text('NULL::character varying'))
    adr_postale_1 = mapped_column(String(255), server_default=text('NULL::character varying'))
    adr_postale_2 = mapped_column(String(255), server_default=text('NULL::character varying'))
    adr_postale_3 = mapped_column(String(2555), server_default=text('NULL::character varying'))
    adr_postaleinsee = mapped_column(String(5), server_default=text('NULL::character varying'))
    adr_postaltel = mapped_column(String(10), server_default=text('NULL::character varying'))
    adr_mail = mapped_column(String(255), server_default=text('NULL::character varying'))
    adr_exploi_1 = mapped_column(String(255), server_default=text('NULL::character varying'))
    adr_exploi_2 = mapped_column(String(255), server_default=text('NULL::character varying'))
    adr_exploi_3 = mapped_column(String(255), server_default=text('NULL::character varying'))
    adr_exploinsee = mapped_column(BigInteger)
    adr_exploitel = mapped_column(String(255), server_default=text('NULL::character varying'))
    adr_portable1 = mapped_column(String(255), server_default=text('NULL::character varying'))
    adr_portable2 = mapped_column(String(255), server_default=text('NULL::character varying'))
    adr_postalcp = mapped_column(String(255), server_default=text('NULL::character varying'))
    adr_exploitcp = mapped_column(String(255), server_default=text('NULL::character varying'))


class TUsager(Base):
    __tablename__ = 't_usager'
    __table_args__ = (
        PrimaryKeyConstraint('idt_usager', name='t_usager_pkey'),
    )

    idt_usager = mapped_column(BigInteger)
    u_pacage = mapped_column(String(9), server_default=text('NULL::character varying'))
    u_civilite = mapped_column(String(12), server_default=text('NULL::character varying'))
    u_nom_raison_sociale = mapped_column(String(40), server_default=text('NULL::character varying'))
    u_prenoms = mapped_column(String(30), server_default=text('NULL::character varying'))
    u_forme_juridique = mapped_column(String(50), server_default=text('NULL::character varying'))
    u_siret = mapped_column(String(14), server_default=text('NULL::character varying'))
    u_msa = mapped_column(String(14), server_default=text('NULL::character varying'))
    u_etat = mapped_column(String(10), server_default=text('NULL::character varying'))
    u_date_debut_validite_sigc = mapped_column(String(10), server_default=text('NULL::character varying'))
    u_date_fin_validite_sigc = mapped_column(String(10), server_default=text('NULL::character varying'))
    u_date_cloture = mapped_column(String(10), server_default=text('NULL::character varying'))
    u_civilite_edit = mapped_column(String(30), server_default=text('NULL::character varying'))


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


class City(Base):
    __tablename__ = 'city'
    __table_args__ = (
        ForeignKeyConstraint(['country_id'], ['country.id'], name='city_country_id_fkey'),
        PrimaryKeyConstraint('id', name='city_pkey')
    )

    id = mapped_column(Integer)
    city = mapped_column(String)
    country_id = mapped_column(Integer)

    country: Mapped[Optional['Country']] = relationship('Country', back_populates='city')


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
