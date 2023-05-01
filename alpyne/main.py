from control.manual.server.controller import Controller
from control.manual.server.receiver import Receiver
from control.automatic.a01.launcher import launch
import configparser
import RPi.GPIO as GPIO
from move import Move
import threading
import queue
import sys

CONF_PATH = "alpyne.conf"

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read(CONF_PATH)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    if sys.argv[1] == "man":

        command_queue = queue.Queue()
        move = Move(config["motor.one.pins"], config["motor.two.pins"])
        receiver = Receiver(config["control.manual.bluetooth"])
        controller = Controller(move, command_queue)
        con_thread = threading.Thread(target=controller.run)
        rec_thread = threading.Thread(target=receiver.get_message, args=(command_queue,))
        con_thread.start()
        rec_thread.start()

    elif sys.argv[1] == "a01":

        launch(config)
