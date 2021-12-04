from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = 'something'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///new.db'
db = SQLAlchemy(app)

from api import models