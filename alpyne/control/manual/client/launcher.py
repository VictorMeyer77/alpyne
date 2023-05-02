import configparser
import socket
import keyboard
from keyboard import KEY_DOWN, KEY_UP

CONF_PATH = "alpyne.conf"


class Controller:

    def __init__(self, bluetooth_config):
        self.socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.socket.connect((bluetooth_config["Address"], int(bluetooth_config["port"])))
        self.listening = True

    def _on_press(self, key):
        if key in ["o", "l", "m", "k", "e"]:
            self.socket.send(bytes(key, "UTF-8"))
        else:
            self.socket.send(bytes("n", "UTF-8"))

    def _on_release(self, key):
        if key == "e":
            self.listening = False
        else:
            self.socket.send(bytes("n", "UTF-8"))

    def on_action(self, event):
        if event.event_type == KEY_DOWN:
            self._on_press(event.name)
        elif event.event_type == KEY_UP:
            self._on_release(event.name)


config = configparser.ConfigParser()
config.read(CONF_PATH)

controller = Controller(config["control.manual.bluetooth"])

keyboard.hook(controller.on_action)
while controller.listening:
    pass
