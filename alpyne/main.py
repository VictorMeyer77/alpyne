import RPi.GPIO as GPIO
from time import sleep

# Definition des pins
M1_En = 40
M1_In1 = 38
M1_In2 = 36

# Creation d'une liste des pins pour chaque moteur pour compacter la suite du code
Pins = [[M1_En, M1_In1, M1_In2]]

# Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(M1_En, GPIO.OUT)
GPIO.setup(M1_In1, GPIO.OUT)
GPIO.setup(M1_In2, GPIO.OUT)

# Voir aide dans le tuto
M1_Vitesse = GPIO.PWM(M1_En, 10)
M1_Vitesse.start(10)


def sens1(moteurNum):
    GPIO.output(Pins[moteurNum - 1][1], GPIO.HIGH)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.LOW)
    print("Moteur", moteurNum, "tourne dans le sens 1.")


def sens2(moteurNum):
    GPIO.output(Pins[moteurNum - 1][1], GPIO.LOW)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.HIGH)
    print("Moteur", moteurNum, "tourne dans le sens 2.")


def arret(moteurNum):
    GPIO.output(Pins[moteurNum - 1][1], GPIO.LOW)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.LOW)
    print("Moteur", moteurNum, "arret.")


def arretComplet():
    GPIO.output(Pins[0][1], GPIO.LOW)
    GPIO.output(Pins[0][2], GPIO.LOW)
    GPIO.output(Pins[1][1], GPIO.LOW)
    GPIO.output(Pins[1][2], GPIO.LOW)
    print("Moteurs arretes.")


arretComplet()

while True:
    # Exemple de motif de boucle
    sens1(1)
    sleep(3)
    sleep(3)
    arretComplet()
    sleep(5)
    sens2(1)
    sleep(2)
    arret(1)
    sleep(1)
    sleep(1)
