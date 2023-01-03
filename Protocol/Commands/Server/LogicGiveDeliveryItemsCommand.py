from DataStream.ByteStream import ByteStream
from Logic.Player import Player
from Logic.Helpers import Helpers
import random
from DataBase.DataBase import DataBase

class LogicGiveDeliveryItemsCommand:
    def encode(self):
        # Brawler Randomaizer:

        a = 0
        i = 0
     #   i = random.randint(0, 20)
        droppedChr = 0
        helper = Helpers(self.player)
        dropper = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        droppedChr = random.randint(0, 20)
        if helper.getUnlockedCharacter(droppedChr) == 1:
                get = False
                rews = 1
        else:
                a = 1
                get = True
                rews = 2
        print(get)

        DataBase.replaceValue(self, 'brawlBoxTokens', self.player.brawlBoxTokens - 100)
        self.player.brawlBoxTokens -= 100
        self.writeVInt(10)
        self.writeVInt(1) 
        self.writeVInt(0) 
        self.writeVInt(rews) # reward count
        print(rews)
        #Gold
        if self.player.boxID == 5:
            GoldValue = random.randrange(10, 100)
            DataBase.replaceValue(self, 'gold', self.player.gold + GoldValue)
        else:
            GoldValue = random.randrange(30, 150)
            DataBase.replaceValue(self, 'gold', self.player.gold + GoldValue)
        self.writeVInt(GoldValue) # reward amount
        self.writeDataReference(0, 7)
        self.writeVInt(0)


        #Brawler
        # PowerPoints
        # #Brawler

#        # PowerPoints

#        PPValue = random.randrange(2, 19)

#        PPBrawlers = random.randrange(0, 20)

#        self.writeVInt(PPValue)

#        self.writeDataReference(16, PPBrawlers)

#        self.writeVInt(6)

#        self.writeVInt(0)

#  
        #Brawler
        if i < 1:
            self.writeVInt(1)
            self.writeDataReference(16, droppedChr)
            self.writeVInt(1)
            self.writeVInt(0)
            self.writeVInt(0)
            helper.UnlockBrawler(droppedChr)
        
        for x in range(8):
            self.writeVInt(x)
        
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(1)