from flask import jsonify, render_template

from app import app

# import RPi.GPIO as GPIO
state = 0


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Raspberry Pi User !'}  # fake user
    return render_template('index.html')


@app.route('/toggle')
def toggle_led():
    # GPIO.setwarnings(False)
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(17, GPIO.IN)
    # state = GPIO.input(17)
    # return str(state) + "hello"
    # GPIO.setup(17, GPIO.OUT)

    global state

    if state == 0:
        # GPIO.output(17,GPIO.HIGH)
        # return 'LED is <font color="red"> ON </font>'
        output = {'led': 'ON'}
        state = 1
    else:
        # GPIO.output(17,GPIO.LOW)
        # return 'LED is <font color="gray"> OFF </font>'
        output = {'led': 'OFF'}
        state = 0
    # return render_template('iotpage.html', title = 'Welcome to IOT !', output = output)
    return jsonify(output)
