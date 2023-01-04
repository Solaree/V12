from Packets.Commands.Server.LogicBoxDataCommand import LogicBoxDataCommand
from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage
from Database.DatabaseManager import DataBase
from Logic.Shop import Shop

from Utils.Reader import BSMessageReader

class LogicPurchaseOfferCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.offer_index = self.read_Vint()


    def process(self, crypter):
    	LogicBoxDataCommand(self.client, self.player).send(crypter)
