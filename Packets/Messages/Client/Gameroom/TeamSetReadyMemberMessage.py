from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Database.DatabaseManager import DataBase
from Utils.Reader import BSMessageReader

class TeamSetReadyMemberMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self, crypter):
        ready = 1
        DataBase.replaceGameroomValue(self, 'Ready', ready, "room")
        TeamGameroomDataMessage(self.client, self.player).send(crypter)