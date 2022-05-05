import socket
import threading
import sys
import time
import random
from queue import Queue

# sys.path.append('../src')
from FishData import FishData
from PondData import PondData
from Payload import Payload
import pickle
from server import PORT
# IP = socket.gethostbyname(socket.gethostname())#"0.tcp.ap.ngrok.io"
IP = "0.tcp.ap.ngrok.io"

ADDR = (IP,18448)#19777
# ADDR = (IP, PORT)
MSG_SIZE = 4096
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"
        
class Client:
    def __init__(self,pond):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = IP
        self.port = PORT
        self.addr = ADDR
        self.connected = True
        self.other_ponds = {}
        self.disconnected_ponds = {}
        self.msg = self.connect()
        self.payload = Payload()
        self.pond = pond
        self.messageQ = []

    def get_msg(self):
        while self.connected:
            time.sleep(0.5)
            msg = pickle.loads(self.client.recv(MSG_SIZE))
            if(msg):
                self.messageQ.append(msg)
                self.handle_msg(msg)
            else:
                break
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            print(f"Client connected ")
            return "Connected"
        except:
            print("Can not connect to the server")

    def send_pond(self):
        try:
            while self.connected:
                time.sleep(2)
                self.payload.action = "SEND"
                self.payload.data = self.pond
                print("POND >>>>> "+ str(self.pond))
                #print("Client send :",self.pond)
                self.client.send(pickle.dumps(self.payload))
                #msg =  pickle.loads(self.client.recv(MSG_SIZE))
                #return self.handle_msg(msg)

        except socket.error as e:
            print(e)

    def migrate_fish(self, fishData , destination):
        ### Migration takes a special object for the payload to pickup : The destination pond's name 
        try:

            migration = {
                "destination" : destination,
                "fish" : fishData
            }
            self.payload.action = "MIGRATE"
            self.payload.data = migration

            self.client.send(pickle.dumps(self.payload))
            print("=======MIGRATED=======")            
            ### Handle our fish in the pond
            # // TO BE IMPLEMENTED

            # msg =  pickle.loads(self.client.recv(MSG_SIZE))
            # return self.handle_msg(msg)
            

            # print("Client send :",pond)
            # next_pond = random.random_choice(self.other_ponds.keys())
            # self.client.send("MIGRATE FROM sick_salmon TO "+ next_pond + " " + pickle.dumps(fishData))
            # msg =  pickle.loads(self.client.recv(MSG_SIZE))
            # return self.handle_msg(msg)
        except socket.error as e:
            print(e)
    
    def disconnect(self) :
        try:
            self.connected = False
            self.payload.action = DISCONNECT_MSG
            print("Disconnecting...")
            self.client.send(pickle.dumps(self.payload))
            return self.client.recv(MSG_SIZE)

        except socket.error as e:
            print(e)

    def handle_lifetime( self ):
        while self.connected:
            if (len(self.other_ponds.keys()) > 0):
                for k, v in self.other_ponds.items():
                    temp = self.other_ponds[k].fishes
                    for i in range(len(temp)):
                        temp[i].lifetime -= 1
                    self.other_ponds[k].fishes = []
                    for i in range(len(temp)):
                        if (temp[i].lifetime > 0):
                            self.other_ponds[k].fishes.append(temp[i])

            time.sleep(1)

    def handle_msg(self, msg):
        msg_action = msg.action
        msg_object = msg.data

        if(msg_action == "SEND" and self.pond.pondName != msg_object.pondName) :
            self.other_ponds[msg_object.pondName] = msg_object #Update in the dict key = pondname, values = <PondData>
            if (msg_object.pondName in self.disconnected_ponds.keys()):
                self.disconnected_ponds.pop(msg_object.pondName)
            print(self.other_ponds)
            return msg
        
        elif(msg_action == "MIGRATE"):
            if(self.pond.pondName == msg_object["destination"]):
                print("=======RECIEVED MIGRATION=======")
                self.pond.addFish(msg_object["fish"])
                print(self.pond.fishes)
                print("================================")
        
        elif(msg_action == DISCONNECT_MSG):
            print("DIS ACTION",msg_action)
            print("DIS OBJECT",msg_object)
            self.disconnected_ponds[msg_object.pondName] = msg_object
            self.other_ponds.pop(msg_object.pondName)

            # time.sleep(10)
        # print(self.other_ponds, self.disconnected_ponds)
        return msg

        # if msg[:7] == "MIGRATE":
        #     pass
        # elif msg[:4] == "JOIN":
        #     pass
        # elif msg[:11] == "DISCONNECT":
        #     pass
        # else:
        #     print(f"Vivisystem : {msg}")
        #     return msg

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


    # def __init__(self):
    #     self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     self.server = IP
    #     self.port = PORT
    #     self.addr = ADDR
    #     self.connected = True
    #     self.other_ponds = {}
    #     self.msg = self.connect()

    # def get_msg(self):
    #     return self.msg
    
    # def connect(self):
    #     try:
    #         self.client.connect(self.addr)
    #         print(f"Client connected ")
    #         return "Connected"
    #     except:
    #         print("Can not connect to the server")

    # def send_pond(self,pond):
    #     try:
    #         print("Client send :",pond)
    #         self.client.send(pickle.dumps(pond))
    #         msg =  pickle.loads(self.client.recv(MSG_SIZE))
            
    #         return self.handle_msg(msg)
    #     except socket.error as e:
    #         print(e)

    # def migrate_fish( self, fishData):
    #     try:
    #         print("Client send :",pond)
    #         next_pond = random.random_choice(self.other_ponds.keys())
    #         self.client.send("MIGRATE FROM sick_salmon TO "+ next_pond + " " + pickle.dumps(fishData))
    #         msg =  pickle.loads(self.client.recv(MSG_SIZE))
    #         return self.handle_msg(msg)
    #     except socket.error as e:
    #         print(e)

    # def handle_msg(self, msg):
    #     return msg
    #     if msg[:7] == "MIGRATE":
    #         pass
    #     elif msg[:4] == "JOIN":
    #         pass
    #     elif msg[:11] == "DISCONNECT":
    #         pass
    #     else:
    #         print(f"Vivisystem : {msg}")
    #         return msg