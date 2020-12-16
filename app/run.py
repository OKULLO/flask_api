from flask import Flask, request,Response
from config.settings import format_url
from flask_sqlalchemy import SQLAlchemy
from schema.models import db



def create_app():

      app = Flask(__name__)
      app.config.from_object('config.settings')
      app.config['SQLALCHEMY_DATABASE_URI'] = format_url('postgresql')
      app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
      app.app_context().push()
      db.init_app(app)
      db.create_all()

      return app

if __name__ == "__main__":
    entry = create_app()
    entry.run(host='0.0.0.0', port=5000, debug=True)