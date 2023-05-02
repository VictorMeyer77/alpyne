class Controller:

    def __init__(self, move):

        self.move = move

    def run(self, environment_info):
        distance = float(environment_info["ultrasonic_distance"])
        if distance > 30.0:
            self.move.forward()
        else:
            self.move.right()

