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

all_connections = {}


def handle_pond(connection, address):
    print(f"New pond connected from : {address}")

    connected = True
    while connected:
        message = connection.recv(MSG_SIZE).decode(FORMAT)
        if message == DISCONNECT_MSG:
            connected = False
            del all_connections[address]
            for addr, conn in all_connections.items():
                conn.send(f"{address} disconnected.".encode(FORMAT))
        
        print(f"{address} : {message}")
        for addr, conn in all_connections.items():
            print(addr, conn)
            conn.send(message.encode(FORMAT))

    connection.close()

if __name__ == "__main__":
    print("Starting vivisystem...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen(5)
    print(f"Vivisystem is listening on {IP}:{PORT}")

    while True:
        add, con = server.accept()
        if (type(add) == tuple):
            clientAddress = add
            clientConnection = con
        else:
            clientAddress = con
            clientConnection = add

        all_connections[clientAddress] = clientConnection

        pond_handler = threading.Thread(target=handle_pond, args=(clientConnection, clientAddress,))
        pond_handler.start()
        print(f"Ponds in the vivisystem: {threading.activeCount() - 1} {clientConnection} {clientAddress}")
