import os
import sqlite3
from flask import Flask
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
modus = Modus(app)
modus.init_app(app)
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 8000
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.sqlite3'

db = SQLAlchemy(app)