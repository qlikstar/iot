from flask import Flask
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float

from flask.ext.cors import CORS

app = Flask(__name__, static_url_path='')

cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iot.db'
db = SQLAlchemy(app)


class IotDevices(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=False)
    price = Column(Float, nullable=False)


db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(IotDevices, methods=['GET', 'PUT', 'POST', 'DELETE'])

from app import views
