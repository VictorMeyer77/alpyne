import time


class Controller:

    def __init__(self, move, queue, camera):
        self.move = move
        self.queue = queue
        self.camera = camera

    def run(self):
        while True:
            if not self.queue.empty():
                command = self.queue.queue[-1]
                if command == "e":
                    break
                else:
                    self.execute_command(command)

    def execute_command(self, command):
        if command == "o":
            self.move.forward()
        elif command == "l":
            self.move.backward()
        elif command == "m":
            self.move.right()
        elif command == "k":
            self.move.left()
        elif command == "n":
            self.move.stop()

        if command in ["o", "l", "m", "k"]:
            self.camera.capture(command)
        time.sleep(0.25)
