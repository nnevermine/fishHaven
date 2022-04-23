import socket
import threading
import sys
import time
from queue import Queue

IP = socket.gethostbyname(socket.gethostname())
PORT = 7015
ADDR = (IP, PORT)
MSG_SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

if __name__ == "__main__":
    pond = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pond.connect(ADDR)
    print(f"Client connected ")

    connected = True
    while connected:
        msg = "hi"

        pond.send(msg.encode(FORMAT))

        if msg == DISCONNECT_MSG:
            connected = False
        else:
            msg = pond.recv(MSG_SIZE).decode(FORMAT)
            print(f"Vivisystem : {msg}")
