from alpyne.control.manual.launcher import launch as manual_launcher
from control.automatic.a01.launcher import launch as a01_launcher
import configparser
import RPi.GPIO as GPIO
import sys

CONF_PATH = "alpyne.conf"

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read(CONF_PATH)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    if sys.argv[1] == "man":
        manual_launcher(config)

    elif sys.argv[1] == "a01":
        a01_launcher(config)

    GPIO.cleanup()
