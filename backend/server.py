import socket

# AF_INET = IPv4 SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind to ip and port
PORT = 8000
#gethostname() is localhost need to be changed later 
s.bind((socket.gethostname(), PORT))
#queue of 5
s.listen(5)

while True:
    # socket object and client's ip
    clientsocket, address = s.accept() 
