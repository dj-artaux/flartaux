import sys
import platform
import flask
import re
import logging
import os

from flask import Response
from io import BytesIO
from flask import Flask, send_file

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
from sqlalchemy import desc, text

import csv
import io
#from io import StringIO
from flask import make_response

import csv
from io import StringIO
#import StringIO       # allows you to store response object in memory instead of on disk
from flask import Flask, make_response # Necessary imports, should be obvious

from sqlalchemy import text

from openpyxl import Workbook
from flask import Response
from sqlalchemy import inspect

from sqlalchemy import column
import datetime
#from flask_http_response import success, result, error

#from app.models import DataModelTbl #inherits from DB.Model
#from db import DataModelTbl #inherits from DB.Model

from flask import Response
from openpyxl import Workbook
#from openpyxl.writer.excel import save_virtual_workbook
import flask_excel as excel


import pandas as pd
import io
from flask import make_response

from flask import Flask, render_template
from flask_htmx import HTMX

@dbinstance.route('/book_list')
def book_list():
    #books = Book.objects.all()
    #param = '%%jd%%'
    #books = Book.objects.raw("SELECT * FROM book WHERE title LIKE %s", [param])
    #books = Book.objects.raw("SELECT * FROM book WHERE title LIKE '%%i%%'")
   
    param = '%%%%%'
    param_date_pub_pref = '20240320'
    param_date_complet_1 = '20240307'
    param_date_complet_2 = '20240320'
    param_ccodro = 'P'
    param_com_in_1 = '22046'
    param_com_in_2 = '22050'
    param_par_idsuf = '222800000C0200'
    
#    books = Book.objects.raw("SELECT DISTINCT 1 as id, libelle, "
    #with connection.cursor() as cursor:
     #   cursor.execute("SELECT DISTINCT libelle, "
    #cursor = connection.cursor()
    #cursor.execute("SELECT DISTINCT libelle, "
    with db.engine.begin() as conn:
        ResultSet = conn.execute(text("SELECT DISTINCT libelle, "
    "array_to_string(array_agg(CONCAT(w, z, x, y) "
    "order by z asc, x asc, y asc), ' - ') "
        "as parcelles, "
        "REPLACE(TO_CHAR(SUM(CAST(REPLACE( par_surface, ',','.') "
        "AS double precision)), '000.9999'), '.',',') as superficie, "
        "nomproprietaireoumandataire, adresseproprietaireoumandataire, "
        "demandeur, adrdem, cedant, no_interne, date_complet/*, u_pacage, "
        "u_nom_raison_sociale, "
        "ROW_NUMBER() OVER(ORDER BY libelle ASC) as id, libelle*/ from "
        "(SELECT DISTINCT libelle, "
        "CONCAT (SUBSTRING(t_parceldem.par_idsuf, 1, 2), "
        "SUBSTRING(t_parceldem.par_idsuf, 6, 3)), par_idsuf, par_surface, "
        "concat(t_parceldem.par_idsuf, ' ') AS u, "
        "SUBSTRING ( RIGHT( par_idsuf, 10 ) FROM '[A-Z]+') AS z, "
        "regexp_replace(SUBSTRING ( RIGHT( par_idsuf, 6 ) "
        "FROM '[0-9]+[_\\d]+' ), '(^|-)0*', '', 'g')::int as x, "
        "SUBSTRING( par_idsuf, 6, 3 ) as w, "
        "SUBSTRING ( RIGHT( par_idsuf, 6 ) FROM '[A-Z]+$' ) AS y, "
        "replace(regexp_replace(CONCAT(array_agg(ddenom)),'{|}| |\"',' ','gi'), ',',CHR(13)) as nomproprietaireoumandataire, "
        "replace(regexp_replace(CONCAT(array_agg(dlign6)),'{|}| |\"',' ','gi'), ',',CHR(13)) as adresseproprietaireoumandataire, "
        "/*u_pacage, concat(u_nom_raison_sociale,*/ "
        "  u_nom_raison_sociale AS demandeur, /*adr_postalcp,*/ "
        "(select distinct adr_postalcp FROM t_usadresse "
    "RIGHT JOIN t_demande "
    "ON no_pacage_demandeur = u_pacage "
    "RIGHT JOIN t_usager "
    "ON no_pacage_demandeur = adr_pacage "
    " WHERE t_demande.no_interne = par_nointerne) AS adrdem, "
    "(select distinct concat( "
    "u_nom_raison_sociale, ' ', adr_postalcp) AS zut FROM t_usager "
    "RIGHT JOIN t_demande "
    "ON no_pacage_cedant = u_pacage "
    "RIGHT JOIN t_usadresse "
    "ON no_pacage_cedant = adr_pacage "
    " WHERE t_demande.no_interne = par_nointerne) AS cedant, "
"    par_idpropr, no_interne, date_complet FROM t_parceldem "
    "      LEFT JOIN t_demande "
    "    ON t_parceldem.par_nointerne = t_demande.no_interne "
    " /*INNER JOIN t_mvtcommune "
    "    ON t_parceldem.par_insee = CAST (t_mvtcommune.comav AS INT)*/ "
" /* "
    "      LEFT JOIN t_mvtcommune "
    "    ON comap LIKE CONCAT(SUBSTRING(t_parceldem.par_idsuf, 1, 2), "
"    CASE WHEN SUBSTRING(t_parceldem.par_idsuf, 6, 3) LIKE '000' THEN "
" SUBSTRING(t_parceldem.par_idsuf, 3, 3) "
    "       ELSE CONCAT(SUBSTRING(t_parceldem.par_idsuf, 1, 2) "
"    "
    "SUBSTRING(t_parceldem.par_idsuf, 3, 3)) END) "
"*/   "        
    "      RIGHT JOIN t_com2023 "
    "      /*ON com = CONCAT('22', SUBSTRING( par_idsuf, 6, 3 ))*/ "
    "    ON com LIKE CONCAT(SUBSTRING(t_parceldem.par_idsuf, 1, 2), "
"    CASE WHEN SUBSTRING(t_parceldem.par_idsuf, 6, 3) LIKE '000' THEN "
" SUBSTRING(t_parceldem.par_idsuf, 3, 3) "
    "       ELSE CONCAT(SUBSTRING(t_parceldem.par_idsuf, 1, 2), "
    "SUBSTRING(t_parceldem.par_idsuf, 3, 3)) END) "
    "       AND libelle IN(SELECT libelle FROM t_com2023 "
"WHERE dep = '22') "
           "OR com LIKE CONCAT(SUBSTRING(t_parceldem.par_idsuf, 1, 2), "
           "SUBSTRING(t_parceldem.par_idsuf, 3, 3)) AND libelle  "
           "IN(SELECT libelle FROM t_com2023 "
"WHERE dep = '22') "
          "/*ON com LIKE CONCAT(SUBSTRING(t_parceldem.par_idsuf, 1, 2), "
"          CASE WHEN SUBSTRING(t_parceldem.par_idsuf, 6, 3) LIKE '000' THEN "
" SUBSTRING(t_parceldem.par_idsuf, 3, 3) "
          " ELSE CONCAT(SUBSTRING(t_parceldem.par_idsuf, 1, 2), "
          "SUBSTRING(t_parceldem.par_idsuf, 3, 3)) END)*/ "
          "/*LIKE CAST(t_parceldem.par_insee AS TEXT)*/ "         
          "RIGHT JOIN t_usager "
        "ON t_demande.no_pacage_demandeur = t_usager.u_pacage "
         " RIGHT JOIN t_proprietaires "
        "ON t_parceldem.par_idpropr = t_proprietaires.idprocpte  "
		 " WHERE t_parceldem.par_idsuf IN "
		  " (SELECT DISTINCT t_parcel_statut.par_idsuf FROM "
"          t_parcel_statut, t_parceldem  "
			"WHERE t_parceldem.par_idsuf = t_parcel_statut.par_idsuf  "
			"AND t_parcel_statut.no_interne = t_parcel_statut.no_interne_pub "
"AND date_pub_pref = '20240425') "
"		  AND date_complet BETWEEN '20240412' and '20240424' "
" AND ccodro LIKE 'X' AND suppr IS FALSE /*"
" AND com IN ('22046', '22050') "
" OR t_parceldem.par_idsuf LIKE '222800000C0200'*/ "        
"GROUP BY t_parceldem.par_idpropr, date_complet, "
" par_nointerne, libelle, "
"        t_demande.no_interne, t_usager.u_pacage, "
" t_usager.u_nom_raison_sociale, t_parceldem.par_idsuf, "
"        t_parceldem.par_surface ORDER BY  "
"adresseproprietaireoumandataire ASC, nomproprietaireoumandataire asc, "
" no_interne desc) as bof "
"        GROUP BY bof.date_complet, bof.demandeur, "
" bof.adrdem, bof.cedant, bof.libelle, bof.no_interne, "
"		bof.adresseproprietaireoumandataire, bof.nomproprietaireoumandataire/*, "
"        bof.u_pacage, bof.u_nom_raison_sociale*/ ORDER BY libelle ASC, parcelles ASC, bof.no_interne DESC"))
#[param_date_pub_pref,
#    param_date_complet_1, param_date_complet_2, param_ccodro,
#    param_com_in_1, param_com_in_2, param_par_idsuf])
        
#ResultSet = text("SELECT * FROM attendance WHERE user_id = :x")
#ResultSet = ResultSet.bindparams(x="1")
#res = session.execute(ResultSet).all()
        '''
        ResultSet = ResultSet.bindparams(param_date_pub_pref="20240320",
        param_date_complet_1="20240320", param_date_complet_2="20240320",
        param_ccodro="P", param_com_in_1="22046", param_com_in_2="22050",
        param_par_idsuf="222800000C0200")
        '''
        books = ResultSet.fetchall()
        for row in books:
            print("%s, %s" % (row[0], row[1]))
            
    return render_template('book_list.html', books=books)
