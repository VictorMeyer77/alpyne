class Controller:

    def __init__(self, move, queue):
        self.move = move
        self.queue = queue

    def run(self):
        while True:
            command = self.queue.get()
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
