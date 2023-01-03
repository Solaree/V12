from DataStream.ByteStream import ByteStream
from Logic.Player import Player

class MatchmakingStopMessage(ByteStream):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20406
        self.player = player

    def encode(self):
        pass