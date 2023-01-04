from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Logic.EventSlots import EventSlots
from Database.DatabaseManager import DataBase
import random
from random import choice
from string import ascii_uppercase
import json
from Utils.Reader import BSMessageReader


class TeamCreateMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.mapSlot = self.read_Vint()
        self.player.map_id = self.read_Vint()
        self.roomType = self.read_Vint()
        self.mapID = self.read_Vint()

    def process(self, crypter):
        self.player.room_id = random.randint(0, 2147483647)
        DataBase.replaceValue(self, 'roomID', self.player.room_id)

        DataBase.createGameroomDB(self)
        TeamGameroomDataMessage(self.client, self.player).send(crypter)
