from flask import Flask
from flask.ext.restful import Api, Resource

app = Flask(__name__)
api = Api(app)
from app.views import views

