from Database.DatabaseManager import DataBase

from Utils.Reader import BSMessageReader
from Files.CsvLogic.Cards import Cards

class LogicSelectSkinCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.player.skin_id = self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.player.brawler_id = self.read_Vint()


    def process(self, crypter):
        DataBase.replaceValue(self, 'skinID', self.player.skin_id)
        self.player.brawlers_skins[str(self.player.brawler_id)] = self.player.skin_id
        DataBase.replaceValue(self, 'brawlersSkins', self.player.brawlers_skins)
        DataBase.replaceValue(self, 'brawlerID', self.player.brawler_id)
        
