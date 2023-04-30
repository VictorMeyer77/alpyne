import RPi.GPIO as GPIO
from time import sleep
import configparser

CONF_PATH = "alpyne.conf"

config = configparser.ConfigParser()
config.read(CONF_PATH)

motor_one_pins = config["motor.one.pins"]
motor_two_pins = config["motor.two.pins"]

# Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


def init():
    GPIO.setup(int(motor_one_pins["Enable"]), GPIO.OUT)
    GPIO.setup(int(motor_one_pins["InputOne"]), GPIO.OUT)
    GPIO.setup(int(motor_one_pins["InputTwo"]), GPIO.OUT)

    GPIO.setup(int(motor_two_pins["Enable"]), GPIO.OUT)
    GPIO.setup(int(motor_two_pins["InputOne"]), GPIO.OUT)
    GPIO.setup(int(motor_two_pins["InputTwo"]), GPIO.OUT)

    # Voir aide dans le tuto
    M1_Vitesse = GPIO.PWM(int(motor_one_pins["Enable"]), 100)
    M2_Vitesse = GPIO.PWM(int(motor_two_pins["Enable"]), 100)
    M1_Vitesse.start(100)
    M2_Vitesse.start(100)

def motor_forward(motor_pins):
    print("GPIO {} to HIGH and {} to LOW".format(motor_pins["InputOne"], motor_pins["InputTwo"]))
    GPIO.output(int(motor_pins["InputOne"]), GPIO.HIGH)
    GPIO.output(int(motor_pins["InputTwo"]), GPIO.LOW)


def motor_backward(motor_pins):
    GPIO.output(int(motor_pins["InputOne"]), GPIO.LOW)
    GPIO.output(int(motor_pins["InputTwo"]), GPIO.HIGH)


def motor_stop(motor_pins):
    print("GPIO {} and {} to LOW".format(motor_pins["InputOne"], motor_pins["InputTwo"]))
    GPIO.output(int(motor_pins["InputOne"]), GPIO.LOW)
    GPIO.output(int(motor_pins["InputTwo"]), GPIO.LOW)


def forward():
    motor_forward(motor_one_pins)
    motor_forward(motor_two_pins)


def backward():
    motor_backward(motor_one_pins)
    motor_backward(motor_two_pins)


def right():
    motor_stop(motor_two_pins)
    motor_forward(motor_one_pins)


def left():
    motor_stop(motor_one_pins)
    motor_forward(motor_two_pins)


def stop():
    motor_stop(motor_one_pins)
    motor_stop(motor_two_pins)

init()
stop()
forward()
sleep(3)
stop()
