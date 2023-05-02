import time


class Controller:

    def __init__(self, move):

        self.move = move

    def run(self, environment_info):
        distance = float(environment_info["ultrasonic_distance"])
        print(distance)
        if distance > 40.0:
            self.move.forward()
        else:
            self.move.right()

