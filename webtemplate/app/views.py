from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello from Raspberry Pi! ... Welcome to the world of IOT :) "

