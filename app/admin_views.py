from app import app
from flask import request, Response
from schema.models import *

@app.route('/create_user')
def create_user():
  request_data = request.get_json()
  new_usr = User(username =request_data['username'],email =request_data['password'],password =request_data['password'])

  