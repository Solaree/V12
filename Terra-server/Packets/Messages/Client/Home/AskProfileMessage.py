from Packets.Messages.Server.Home.PlayerProfileMessage import PlayerProfileMessage
from Database.DatabaseManager import DataBase
from random import choice
from string import ascii_uppercase
import json
from Utils.Reader import BSMessageReader


class AskProfileMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.high_id = self.read_int()
        self.low_id = self.read_int()


    def process(self, crypter):
        self.players = DataBase.getAllPlayers(self)
        PlayerProfileMessage(self.client, self.player, self.high_id, self.low_id, self.players).send(crypter)