import queue
import threading
from move import Move
from control.manual.server.receiver import Receiver
from control.manual.server.controller import Controller


def launch(config):
    command_queue = queue.Queue()
    move = Move(config["motor.one.pins"], config["motor.two.pins"])
    receiver = Receiver(config["control.manual.bluetooth"])
    controller = Controller(move, command_queue)
    con_thread = threading.Thread(target=controller.run)
    rec_thread = threading.Thread(target=receiver.get_message, args=(command_queue,))
    con_thread.start()
    rec_thread.start()
    con_thread.join()
    rec_thread.join()

