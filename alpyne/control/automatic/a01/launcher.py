import queue
import threading
from move import Move
from control.automatic.a01.controller import Controller
from control.sensor.ultrasonic import Ultrasonic


def launch(config):
    ultrasonic_queue = queue.Queue()
    move = Move(config["motor.one.pins"], config["motor.two.pins"])
    move.forward()
    ultrasonic = Ultrasonic(config["ultrasonic.pins"], ultrasonic_queue)
    controller = Controller(move, ultrasonic_queue)
    con_thread = threading.Thread(target=controller.run)
    ult_thread = threading.Thread(target=ultrasonic.start)
    con_thread.start()
    ult_thread.start()
    con_thread.join()
    ult_thread.join()
