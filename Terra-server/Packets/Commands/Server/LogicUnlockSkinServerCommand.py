from Utils.Writer import Writer
from Database.DatabaseManager import DataBase

class LogicUnlockSkinServerCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        # 1 - brawler
        # 2 token doubler
        # 3 - ticket
        # 6 - power point
        # 7 - coin
        # 8 = gem
        self.writeVint(203)
        self.writeVint(100)
        self.writeVint(1)
        self.writeVint(1)
        
        self.writeVint(1) # reward count
        #One Reward
        self.writeVint(1) # item count
        self.writeVint(16) # data reference + 1
        self.writeVint(self.player.brawler_id)
        self.writeVint(9) # rewardID
        self.writeVint(29)
        self.writeVint(self.player.skin_id)
        self.writeVint(0)
        DataBase.appendElementToArray(self, 'ownSkinsArray', self.player.skin_id)
        # end
        for x in range(8):
            self.writeVint(x)
        
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        
        print("[INFO] Message LogicGiveDeliveryItemsCommand has been sent.")