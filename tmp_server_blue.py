"""
A simple Python script to receive messages from a client over
Bluetooth using Python sockets (with Python 3.3 or above).
"""

import socket

hostMACAddress = 'DC:A6:32:C5:38:27'
port = 3
backlog = 1
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
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
