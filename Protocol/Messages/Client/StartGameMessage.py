from DataStream.ByteReader import ByteReader
from Logic.Player import Player
from Logic.Battle.LogicBattle import LogicBattle
from Protocol.Messages.Server.MatchmakingStopMessage import MatchmakingStopMessage
from threading import Thread

class StartGameMessage(ByteReader):
    def __init__(self, client, crypto, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.crypto = crypto
        self.player = player

    def decode(self):
        pass

    def process(self):
        MatchmakingStopMessage(self.client, self.player).send(self.crypto)
        #battle = LogicBattle(self.client, self.crypto, self.player)
       # battle.start()