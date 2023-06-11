import time
import numpy as np


class Controller:

    def __init__(self, move, camera, brain):

        self.move = move
        self.camera = camera
        self.brain = brain

    def run(self):
        view = (self.camera.to_array() / 255.0).astype("float32")
        view = np.reshape(view, (1, 64, 64, 3))
        direction = self.brain.predict(view)
        if direction == 0:
            self.move.forward()
        elif direction == 1:
            self.move.right()
        elif direction == 2:
            self.move.left()
        elif direction == 3:
            self.move.backward()
        else:
            print(f"Unknown direction {direction}")
        time.sleep(0.5)
