import socket
import os
from Network.ClientConnection import ClientConnection
import time

class Server:
    def __init__(self):
        self.server = socket.socket()
        self.listening = True

    def start(self):
        banns = []
        self.server.bind(('0.0.0.0', 9339)) #ServerSocket bind
        print('Server started!')
        while self.listening:
            self.server.listen()
            client, addr = self.server.accept()
            if addr[0] not in banns:
            	print(f'New connection from {addr[0]}')
            	ClientConnection(client, addr, banns).start()
            	banns.append(addr[0])
            else:
            	os.system(f"iptables -A INPUT -s {addr[0]} -j DROP")
            #	time.sleep(15)
            #	banns.remove(addr[0])
            	