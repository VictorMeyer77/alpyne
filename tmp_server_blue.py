"""
A simple Python script to receive messages from a client over
Bluetooth using Python sockets (with Python 3.3 or above).


import socket

hostMACAddress = 'DC:A6:32:C5:38:27'
port = 4
backlog = 1
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
try:
    client, address = s.accept()
    while 1:
        data = client.recv(size)
        if data:
            print(data)
            client.send(data)
except:
    print("Closing socket")
    client.close()
    s.close()
"""

import socket
import time

class Receiver:

    def __init__(self, bluetooth_config):
        self.socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.socket.bind((bluetooth_config["Address"], bluetooth_config["Port"]))
        self.socket.listen(1)
        self.client, self.address = self.socket.accept()

    def get_last_message(self):
        data = self.client.recv(1024)
        if data:
            return data.decode("utf-8")[0]
        else:
            ""

    def close(self):
        self.socket.close()
        self.client.close()

v = Receiver({"Address": "DC:A6:32:C5:38:27", "Port": 4})
while True:
    print(v.get_last_message())
    time.sleep(5)