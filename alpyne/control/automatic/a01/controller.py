import time


class Controller:

    def __init__(self, move, ultrasonic_queue):

        self.move = move
        self.ultrasonic_queue = ultrasonic_queue

    def run(self):
        while True:
            if self.ultrasonic_queue.get() > 50.0:
                self.move.forward()
            else:
                self.move.right()
                time.sleep(2)
                self.move.stop()

