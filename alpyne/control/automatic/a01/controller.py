import time


class Controller:

    def __init__(self, move):

        self.move = move

    def run(self, environment_info):
        tmp = float(environment_info["ultrasonic_distance"])
        print(tmp)
        if tmp > 50.0:
            self.move.forward()
            print("move forward")
        else:
            self.move.right()
            print("move right")
            #self.move.stop()

