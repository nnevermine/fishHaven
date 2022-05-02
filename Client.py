import socket
import threading
import sys
import time
import random
from queue import Queue

# sys.path.append('../src')
from FishData import FishData
from PondData import PondData
import pickle
IP = socket.gethostbyname(socket.gethostname())
PORT = 8003
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
        f = FishData("Sick Salmon","123456")
        print("Client send :",f)
        msg = pickle.dumps(f)
        # message = bytes(f'{len(msg):<{HEADER}}',FORMAT) + msg
        #"MIGRATE FROM .... TO ...." + msg(fish class)
        # msg = "hi"
        pond.send(msg) #.encode(FORMAT)
            # self.client.send(pickle.dumps(data))
            # return pickle.loads(self.client.recv(2048))
        if msg == DISCONNECT_MSG:
            connected = False
        else:
            msg = pickle.loads(pond.recv(MSG_SIZE))#.decode(FORMAT)
            print(f"Vivisystem : {msg}")
        time.sleep(5)
        

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = IP
        self.port = PORT
        self.addr = ADDR
        self.connected = True
        self.other_ponds = {}
        self.msg = self.connect()

    def get_msg(self):
        return self.msg
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            print(f"Client connected ")
            return "Connected"
        except:
            print("Can not connect to the server")

    def send_pond(self,pond):
        try:
            print("Client send :",pond)
            self.client.send(pickle.dumps(pond))
            msg =  pickle.loads(self.client.recv(MSG_SIZE))
            
            return self.handle_msg(msg)
        except socket.error as e:
            print(e)

    def migrate_fish( self, fishData):
        try:
            print("Client send :",pond)
            next_pond = random.random_choice(self.other_ponds.keys())
            self.client.send("MIGRATE FROM sick_salmon TO "+ next_pond + " " + pickle.dumps(fishData))
            msg =  pickle.loads(self.client.recv(MSG_SIZE))
            return self.handle_msg(msg)
        except socket.error as e:
            print(e)

    def handle_msg(self, msg):
        return msg
        if msg[:7] == "MIGRATE":
            pass
        elif msg[:4] == "JOIN":
            pass
        elif msg[:11] == "DISCONNECT":
            pass
        else:
            print(f"Vivisystem : {msg}")
            return msg