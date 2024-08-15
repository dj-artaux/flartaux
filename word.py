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

from docxtpl import DocxTemplate
from flask import Response
from io import BytesIO
from flask import Flask, send_file

def save_sample_details(request):
    sample = my_custom_sql2(self='my_custom_sql2')[0:15]
    #sample = my_custom_sql2.fetchall()[0:15]
    #field_names = my_custom_sql3(self='my_custom_sql3')
    template = DocxTemplate("lab_management/word/sample_template.docx")
    
    #rows = cursor.fetchall()

    for row in sample:
        context = { "mince" : row[0] , "demandeur" : row[1] ,
        "adrdem" : row[2] ,
"cedant" : row[3] , "no_interne" : row[4] , "date_complet" : row[5] ,
 "sum" : row[6] , "compar" : row[7] }        
    #template.render(context)
    #template.save('lab_management/word/sample.docx')
    #return redirect('/lab/sample/details/')
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    response["Content-Disposition"] = 'filename="your_doc_name.docx"'
    
    template.render(context)
    template.save(response)
    
    return response
    