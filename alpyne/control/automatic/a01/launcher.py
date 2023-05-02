import queue
import threading
import time
from move import Move
from control.automatic.a01.controller import Controller
from control.sensor.ultrasonic import Ultrasonic


def launch(config):
    ultrasonic_queue = queue.Queue()
    move = Move(config["motor.one.pins"], config["motor.two.pins"])
    ultrasonic = Ultrasonic(config["ultrasonic.pins"])
    controller = Controller(move)

    while True:
        try:
            controller.run({"ultrasonic_distance": ultrasonic.get_distance()})
            time.sleep(1)
        except KeyboardInterrupt:
            break
