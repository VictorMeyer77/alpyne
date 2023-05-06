import time

import RPi.GPIO as GPIO


# Definition des pins
M1_En = 18
M1_In1 = 20
M1_In2 = 16

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(M1_En, GPIO.OUT)
GPIO.setup(M1_In1, GPIO.OUT)
GPIO.setup(M1_In2, GPIO.OUT)



# Voir aide dans le tuto
M1_Vitesse = GPIO.PWM(M1_En, 100)
M1_Vitesse.start(100)


time.sleep(20)