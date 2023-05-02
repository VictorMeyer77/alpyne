import time


class Controller:

    def __init__(self, move):

        self.move = move

    def run(self, environment_info):
        tmp = float(environment_info["ultrasonic_distance"])
        print(tmp)
        if tmp > 30.0:
            self.move.forward()
            print("move forward")
        else:
            self.move.right()
            time.sleep(0.3)
            print("move right")
            self.move.stop()

