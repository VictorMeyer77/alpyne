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
            time.sleep(1)
        else:
            self.move.right()
            print("move right")
            time.sleep(1)
            #self.move.stop()

