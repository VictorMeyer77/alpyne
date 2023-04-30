import keyboard
from keyboard import KEY_DOWN, KEY_UP


class Manual:

    def __init__(self, move):
        self.move = move
        self.listening = True
        self._start()

    def _on_press(self, key):
        print(key)
        if key == "haut":
            self.move.forward()
        elif key == "bas":
            self.move.backward()
        elif key == "droite":
            self.move.right()
        elif key == "gauche":
            self.move.left()

    def _on_release(self, key):
        print(key)
        if key in ["haut", "bas", "gauche", "droite"]:
            self.move.stop()
        if key == "esc":
            self.move.stop()
            self.listening = False

    def _on_action(self, event):
        if event.event_type == KEY_DOWN:
            self._on_press(event.name)
        elif event.event_type == KEY_UP:
            self._on_release(event.name)

    def _start(self):
        keyboard.hook(self._on_action)
        while self.listening:
            pass
