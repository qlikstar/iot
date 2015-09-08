from app import app
from flask import Flask, jsonify
import RPi.GPIO as GPIO
import time

@app.route('/')
@app.route('/index')
def index():
    return "Hello from Raspberry Pi! ... Welcome to the world of IOT :) "

@app.route('/toggle')
def toggle_led():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN)
    state = GPIO.input(17)
    #return str(state) + "hello"
    GPIO.setup(17, GPIO.OUT)
    if (state==0):
        GPIO.output(17,GPIO.HIGH)
        #return 'LED is <font color="red"> ON </font>'
        return jsonify ({'output' : 'ON'})
    else:
        GPIO.output(17,GPIO.LOW)
        #return 'LED is <font color="gray"> OFF </font>'
        return jsonify ({'output' : 'OFF'})
