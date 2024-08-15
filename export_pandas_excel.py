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


@dbinstance.route('/export_pandas_excel')
def export_pandas_excel():

    # Function is defined somewhere else
    with db.engine.begin() as conn:
        ResultSet = conn.execute(text("select colpivot('_test_pivoted',"
"        'SELECT libelle_commune, par_idsuf, u_nom_raison_sociale, no_interne"
" FROM t_parceldem"
" INNER JOIN t_demande"
" ON t_parceldem.par_nointerne = t_demande.no_interne"
" LEFT JOIN t_commune"
" ON CASE WHEN SUBSTRING(t_parceldem.par_idsuf, 6, 3) LIKE ''000''"
" THEN SUBSTRING(t_parceldem.par_idsuf, 1, 5)"
" ELSE CONCAT (SUBSTRING(t_parceldem.par_idsuf, 1, 2),"
" SUBSTRING(t_parceldem.par_idsuf, 6, 3))"
" END  = t_commune.code_insee_commune "
" INNER JOIN t_usager"
" ON t_demande.no_pacage_demandeur = t_usager.u_pacage"
" WHERE par_idsuf like ''22193000ZH0016%''"
" GROUP BY t_demande.date_complet, t_parceldem.par_idsuf,"
" t_demande.no_interne, t_usager.u_pacage, t_usager.u_nom_raison_sociale,"
" t_commune.libelle_commune, t_parceldem.par_surface"
" ORDER BY par_idsuf asc, no_interne desc,"
" libelle_commune asc LIMIT 100', "
" array['libelle_commune', 'par_idsuf'], array['no_interne', 'u_nom_raison_sociale'],"
" '#.par_idsuf', null);"
" select * from _test_pivoted order by libelle_commune, par_idsuf;"))

        rows = ResultSet.fetchall()
        keys = ResultSet.keys()
        #rows = ResultSet._metadata.keys
        data = rows

   
        # Convert result set to pandas data frame and add columns
        df = pd.DataFrame((tuple(t) for t in data),
            columns=keys)
            #columns=('Date ', 'name', 'username', 'description', 'email','','','','','',''))


        # Creating output and writer (pandas excel writer)
        out = io.BytesIO()
        writer = pd.ExcelWriter(out, engine='xlsxwriter')

   
        # Export data frame to excel
        df.to_excel(excel_writer=writer, header=True, index=True, sheet_name='Sheet1')
        #writer.save()
        writer.close()

   
        # Flask create response 
        r = make_response(out.getvalue())

    
        # Defining correct excel headers
        r.headers["Content-Disposition"] = "attachment; filename=export.xlsx"
        r.headers["Content-type"] = "application/x-xls"

    
        # Finally return response
        return r