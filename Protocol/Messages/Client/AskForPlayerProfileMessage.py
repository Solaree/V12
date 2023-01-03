from DataStream.ByteReader import ByteReader
from Protocol.Messages.Server.PlayerProfileMessage import PlayerProfileMessage
from Logic.Player import Player
from Protocol.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage

class AskForPlayerProfileMessage(ByteReader):
    def __init__(self, client, crypto, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.crypto = crypto
        self.player = player

    def decode(self):
        self.High = self.readInt()
        self.Low = self.readInt()

    def process(self):
        PlayerProfileMessage(self.client, self.player, self.Low).send(self.crypto)