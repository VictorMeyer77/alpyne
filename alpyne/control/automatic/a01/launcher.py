import queue
import threading
from move import Move
from control.automatic.a01.controller import Controller
from sensor.ultrasonic import ultrasonic_loop


def launch(config):
    ultrasonic_queue = queue.Queue()
    move = Move(config["motor.one.pins"], config["motor.two.pins"])
    controller = Controller(move, ultrasonic_queue)
    con_thread = threading.Thread(target=controller.run)
    ult_thread = threading.Thread(target=ultrasonic_loop, args=(config["ultrasonic.pins"], ultrasonic_queue))
    con_thread.start()
    ult_thread.start()
