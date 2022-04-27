import socket
import pickle
import sys
import FishData

PORT = 8000
run = True
hostname = socket.gethostname()
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
    sock.connect((hostname,PORT))  
    while run:
        #send fish
        fish = FishData.FishData("Sick Salmon","000000")
        msg =  pickle.dumps(fish)
        sock.send(msg)

        #receive response
        data = socket.recv(1024)
        # data_fish = pickle.loads(data)


        if data.lower().strip() == 'bye':#len(data)<1024:
            # No more of msg
            print(data)
            run = False
    sock.close()

def send(fish):
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect((HOST, PORT))
    # fish = FishData.FishData("Sick Salmon","000000")
    data = pickle.dumps(fish)
    # socket.send(data)
    # socket.close()
        
                

