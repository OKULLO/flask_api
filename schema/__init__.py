from app import app
from flask_sqlalchemy import SQLAlchemy


from service_db import models

def dbconf():
    db = SQLAlchemy(app)