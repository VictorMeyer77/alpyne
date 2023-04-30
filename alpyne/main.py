import configparser
from RPi import GPIO
from control.manual.manual import Manual
from move import Move
import time

CONF_PATH = "alpyne.conf"

config = configparser.ConfigParser()
config.read(CONF_PATH)

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read(CONF_PATH)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    move = Move(config["motor.one.pins"], config["motor.two.pins"])
    #Manual(move)
    move.forward()
    time.sleep(3)
    move.backward()
    time.sleep(3)