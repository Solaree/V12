from Database.DatabaseManager import DataBase
from Packets.Commands.Server.LogicBoxDataCommand import LogicBoxDataCommand

from Utils.Reader import BSMessageReader

class LogicPurchaseBoxCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        for x in range(5):
            self.read_Vint()
        
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.player.box_id = self.read_Vint()

    def process(self, crypter):
        print("BoxID:", self.player.box_id)
        LogicBoxDataCommand(self.client, self.player).send(crypter)
