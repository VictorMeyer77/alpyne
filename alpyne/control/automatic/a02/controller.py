import numpy as np


class Controller:

    def __init__(self, move, camera, brain):

        self.move = move
        self.camera = camera
        self.brain = brain

    def run(self):
        view = (self.camera.to_array() / 255.0).astype("float32")
        view = np.reshape(view, (1, 64, 64, 3))
        print(self.brain.predict(view))
