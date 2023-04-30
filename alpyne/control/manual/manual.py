from pynput import keyboard
from pynput.keyboard import Key


class Manual:

    def __init__(self, move):
        self.move = move
        self.start()

    def on_press(self, key):
        if key == Key.up:
            self.move.forward()
        elif key == Key.down:
            self.move.backward()
        elif key == Key.right:
            self.move.right()
        elif key == Key.left:
            self.move.left()

    def on_release(self, key):
        if key in [Key.up, Key.down, Key.right, Key.left]:
            self.move.stop()
        if key == keyboard.Key.esc:
            self.move.stop()
            return False

    def start(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()
