from app import app
from app.controllers import authentication

@app.route('/')
@app.route('/index')
def index():
    auth = authentication.Authentication()
    auth.authenticate()
    return "Hello from Raspberry Pi! ... Welcome to the world of IOT :) "





