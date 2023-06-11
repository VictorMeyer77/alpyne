

class Controller:

    def __init__(self, move, camera, brain):

        self.move = move
        self.camera = camera
        self.brain = brain

    def run(self):
        view = self.camera.to_array()
        print(self.brain.predict(view))
