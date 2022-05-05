import threading
import time
from Client2 import Client
from FishData import FishData
from PondData import PondData
from Payload import Payload
p = PondData("pla")
f1 = FishData("pla","123456")
f2 = FishData("pla","321412")
f3 = FishData("pla","123456")
p.addFish(f1)
p.addFish(f2)
p.addFish(f3)
connected = True
c = Client(p)
msg_handler = threading.Thread(target=c.get_msg)   
msg_handler.start() 
send_handler = threading.Thread(target=c.send_pond)
send_handler.start()
c.migrate_fish(p.fishes[0],"sick-salmon")
time.sleep(5)
c.migrate_fish(p.fishes[1],"sick-salmon")
time.sleep(10)
c.disconnect()
