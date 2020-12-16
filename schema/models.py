import uuid
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  user_id = db.Column(db.String(80), primary_key=True, default=lambda: str(uuid.uuid4()))
  username = db.Column(db.String(80))
  email = db.Column(db.String(80), unique=True)
  password =db.Column(db.String(80),unique=True,nullable =False)