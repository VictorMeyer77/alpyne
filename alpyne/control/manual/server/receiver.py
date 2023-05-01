import socket


class Receiver:

    def __init__(self, bluetooth_config):
        self.socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.socket.bind((bluetooth_config["Address"], bluetooth_config["Port"]))
        self.socket.listen(1)
        self.client, _ = self.socket.accept()

    def get_message(self, queue):
        while True:
            data = self.client.recv(1024)
            message = data.decode("utf-8")[-1]
            queue.put(message)
            if message == "e":
                self.close()
                break

    def close(self):
        self.socket.close()
        self.client.close()

