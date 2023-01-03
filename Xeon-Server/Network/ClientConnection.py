import time
import os
from threading import *
from NaCl import NaCl
from Protocol.LogicMessageFactory import packets
from Logic.Player import Player
from datetime import datetime
import json
from random import choice as c

class ClientConnection(Thread):
    def __init__(self, client, addr, banns):
        super().__init__()
        self.client = client
        self.addr = addr
        self.banns = banns
        self.crypto = NaCl()
        self.player = Player()

    def recvall(self, length: int):
        data = b''
        while len(data) < length:
            d = self.client.recv(length)
            if not d:
                print("ERROR! (Empty data from client!)")
                break
            data += d
        return data

    def run(self): # client processing thread
        last_packet = time.time()
        try:
            while True:
                if datetime.now().minute == 0 and datetime.now().second == 0:
                	with open("events.json", "r") as jsonFile:
                		data = json.load(jsonFile)
                	data["gems"] = c([7, 8, 9, 10, 11, 12])
                	data["sd"] = c([13, 14, 15, 16])
                	data["dsd"] = data["sd"] + 21
                	data["trio"] = c([1, 2, 3, 4, 5, 6, 22])
                	data["bonus"] = c([24, 25, 26, 17, 18, 19])
                	with open("events.json", "w") as jsonFile:
                		json.dump(data, jsonFile)
                header = self.client.recv(7)
                if len(header) > 0:
                    last_packet = time.time()
                    packet_id = int.from_bytes(header[:2], 'big')
                    length = int.from_bytes(header[2:5], 'big')
                    data = self.recvall(length)
                    pdata = self.crypto.decrypt(packet_id ,data)
                    if packet_id in packets:
                        print(f'Received packet with id: {packet_id}')
                        message = packets[packet_id](self.client, self.crypto, self.player, pdata)
                        message.decode()
                        message.process()
                    else:
                        print(f'Unhandled: {packet_id}')
                if time.time() - last_packet > 3:
                    print(f"{self.addr[0]} disconnected!")
                  #  os.system(f"iptables -A INPUT -s {self.addr[0]} -j ACCEPT")
                    self.client.close()
                    self.banns.remove(self.addr[0])
                    break
        except ConnectionAbortedError:
            print(f"{self.addr[0]} disconnected!")
        #    os.system(f"iptables -A INPUT -s {self.addr[0]} -j ACCEPT")
            self.client.close()
            self.banns.remove(self.addr[0])
        except ConnectionResetError:
            print(f"{self.addr[0]} disconnected!")
          #  os.system(f"iptables -A INPUT -s {self.addr[0]} -j ACCEPT")
            self.client.close()
            self.banns.remove(self.addr[0])
        except TimeoutError:
            print(f"{self.addr[0]} disconnected!")
          #  os.system(f"iptables -A INPUT -s {self.addr[0]} -j ACCEPT")
            self.client.close()
            self.banns.remove(self.addr[0])