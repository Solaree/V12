from Network.Server import Server
from DataBase.DataBase import DataBase
from random import randint as r
#DataBase.loadAll()
import os
import json


print("Starting Server...")

server = Server()
server.start()

