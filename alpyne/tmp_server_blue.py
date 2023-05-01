import configparser
import RPi.GPIO as GPIO

from move import Move
from control.manual.server.controller import Controller
from control.manual.server.receiver import Receiver

import threading
import queue

CONF_PATH = "alpyne.conf"

if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    config = configparser.ConfigParser()
    config.read(CONF_PATH)

    q = queue.Queue()
    move = Move(config["motor.one.pins"], config["motor.two.pins"])
    receiver = Receiver(config["control.manual.bluetooth"])
    controller = Controller(move, q)
    con_thread = threading.Thread(target=controller.run)
    rec_thread = threading.Thread(target=receiver.get_message, args=(q,))
    con_thread.start()
    rec_thread.start()

