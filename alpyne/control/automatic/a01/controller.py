import time


class Controller:

    def __init__(self, move, ultrasonic_queue):

        self.move = move
        self.ultrasonic_queue = ultrasonic_queue

    def run(self):
        try:
            while True:
                tmp = float(self.ultrasonic_queue.get())
                print(tmp)
                if tmp > 50.0:
                    self.move.forward()
                    #time.sleep(3)
                else:
                    self.move.right()
                    #time.sleep(3)
                    #self.move.stop()
        except KeyboardInterrupt:
            pass

