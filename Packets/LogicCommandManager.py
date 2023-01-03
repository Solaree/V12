from Utils.Reader import BSMessageReader
from Packets.Commands.Client.LogicUpgradeBrawler import Upgrade_Brawler
from Packets.Commands.Client.LogicSetPlayerThumbnailCommand import LogicSetPlayerThumbnailCommand
from Packets.Commands.Client.LogicPurchaseBoxCommand import LogicPurchaseBoxCommand
from Packets.Commands.Client.LogicPurchaseOfferCommand import LogicPurchaseOfferCommand
from Packets.Commands.Client.LogicSelectSkinCommand import LogicSelectSkinCommand
from Packets.Commands.Client.LogicPurchaseHeroLvlUpMaterialCommand import LogicPurchaseHeroLvlUpMaterialCommand
from Packets.Commands.Client.LogicPurchaseDoubleCoinsCommand import LogicPurchaseDoubleCoinsCommand
from Database.DatabaseManager import DataBase
from Packets.Commands.Client.LogicUnlockSkinCommand import LogicUnlockSkinCommand

from random import choice
from string import ascii_uppercase
import json
class EndClientTurn(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.commandID = self.read_Vint()


    def process(self, crypter):
        print(self.commandID)
        if self.commandID == 500 or self.commandID == 517 or self.commandID == 535:
            LogicPurchaseBoxCommand.decode(self)
            LogicPurchaseBoxCommand.process(self, crypter)

        elif self.commandID == 519:
            LogicPurchaseOfferCommand.decode(self)
            LogicPurchaseOfferCommand.process(self, crypter)
            
        elif self.commandID == 203:
            if self.player.box_id == 5:
                DataBase.replaceValue(self, 'brawlBoxes', self.player.brawl_boxes - 100)
            elif self.player.box_id == 4:
                DataBase.replaceValue(self, 'bigBoxes', self.player.big_boxes - 10)
            elif self.player.box_id == 3:
                DataBase.replaceValue(self, 'gems', self.player.gems - 80)
            elif self.player.box_id == 2:
                DataBase.replaceValue(self, 'gems', self.player.gems - 30)

        elif self.commandID == 505:
            LogicSetPlayerThumbnailCommand.decode(self)
            LogicSetPlayerThumbnailCommand.process(self, crypter)

        elif self.commandID == 506:
            LogicSelectSkinCommand.decode(self)
            LogicSelectSkinCommand.process(self, crypter)
        
        elif self.commandID == 507:
            LogicUnlockSkinCommand.decode(self)
            LogicUnlockSkinCommand.process(self, crypter)

        elif self.commandID == 520:
            Upgrade_Brawler.decode(self)
            Upgrade_Brawler.process(self, crypter)

        elif self.commandID == 521:
            LogicPurchaseHeroLvlUpMaterialCommand.decode(self)
            LogicPurchaseHeroLvlUpMaterialCommand.process(self, crypter)

        elif self.commandID == 509:
            LogicPurchaseDoubleCoinsCommand.decode(self)
            LogicPurchaseDoubleCoinsCommand.process(self, crypter)

        else:
            print("CommandID:", self.commandID, "not handled!")