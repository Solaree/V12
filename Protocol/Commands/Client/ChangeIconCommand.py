import random
from Logic.Player import Player
from Logic.Helpers import Helpers
from DataStream.ByteReader import ByteReader
from DataBase.DataBase import DataBase

class ChangeIconCommand(ByteReader):
    def __init__(self, client, crypto, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        print(self.readVInt())
        print(self.readVInt())
        print(self.readVInt())
        print(self.readVInt())
        print(self.readVInt())
        print(self.readVInt())
        print(self.readVInt())
        print(self.readVInt())
        print(self.readVInt())
        print(self.readVInt())
        
        self.player.profileIcon = self.readVInt()
        print(self.player.profileIcon)
        


    def process(self):
        DataBase.replaceValue(self, 'profileIcon', self.player.profileIcon)