import threading
from Client2 import Client
from FishData import FishData
from PondData import PondData
from Payload import Payload
p = PondData("pla")
connected = True
c = Client(p)
msg_handler = threading.Thread(target=c.get_msg)   
msg_handler.start() 
send_handler = threading.Thread(target=c.send_pond)
send_handler.start()