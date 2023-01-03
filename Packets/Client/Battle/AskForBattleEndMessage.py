from Packets.Messages.Server.Battle.BattleResultShowdownMessage import BattleResultShowdownMessage
from Packets.Messages.Server.Battle.BattleResultMessage import BattleResultMessage
from Packets.Messages.Server.Battle.BattleResultDuoShowdownMessage import BattleResultDuoShowdownMessage
from random import choice
from string import ascii_uppercase
import json
from Utils.Reader import BSMessageReader


class AskForBattleEndMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.player.battle_result = self.read_Vint()
        unknown = self.read_Vint()
        self.player.rank = self.read_Vint()
        self.map = self.read_Vint() # Selected Map
        self.read_Vint() # Locations CsvID
        self.read_Vint() # Battle End Players
        self.read_Vint() # Brawler CsvID
        self.player.brawler_id = self.read_Vint() # Selected Brawler
        self.read_Vint() # Skin CsvID
        self.read_Vint()
        
        
        print("BATTLE RESULT", self.player.battle_result)
        print("RANK", self.player.rank)
        print("UNKNOWN", unknown)
        print("MAP", self.map)

        self.player.team = self.read_Vint() 
        self.read_Vint() 
        self.read_string() #Your Name

        self.read_Vint()
        self.Bot1 = self.read_Vint() #bot brawler
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()
        self.Bot1N = self.read_string()

        self.read_Vint()
        self.Bot2 = self.read_Vint() #bot brawler
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()
        self.Bot2N = self.read_string()

        self.read_Vint()
        self.Bot3 = self.read_Vint() #bot brawler
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()
        self.Bot3N = self.read_string()

        self.read_Vint()
        self.Bot4 = self.read_Vint() #bot brawler
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()
        self.Bot4N = self.read_string()

        self.read_Vint()
        self.Bot5 = self.read_Vint() #bot brawler
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()
        self.Bot5N = self.read_string()

    def process(self, crypter):

    	if self.player.rank != 0:
            if self.map in [21, 34, 35, 36, 37, 38, 44, 46, 56, 94, 96]:
    	    	    self.player.bot1_n = self.Bot1N
    	    	    self.player.bot1 = self.Bot1
    	    	    BattleResultDuoShowdownMessage(self.client, self.player).send(crypter)
            else:
    	    	    BattleResultShowdownMessage(self.client, self.player).send(crypter)
    	else:
            if self.map in [97]:
    	    	    if self.player.team == 0:

    	    	        self.player.bot1_n = self.Bot1N
    	    	        self.player.bot2_n = self.Bot2N
    	    	        self.player.bot3_n = self.Bot3N
    	    	        self.player.bot4_n = self.Bot4N
    	    	        self.player.bot5_n = self.Bot5N
    	    	        self.player.bot1 = self.Bot1
    	    	        self.player.bot2 = self.Bot2
    	    	        self.player.bot3 = self.Bot3
    	    	        self.player.bot4 = self.Bot4
    	    	        self.player.bot5 = self.Bot5

    	    	        BattleResultMessage(self.client, self.player).send(crypter)
    	    	    else:

    	    	        self.player.bot1_n = self.Bot4N
    	    	        self.player.bot2_n = self.Bot5N
    	    	        self.player.bot3_n = self.Bot3N
    	    	        self.player.bot4_n = self.Bot1N
    	    	        self.player.bot5_n = self.Bot2N
    	    	        self.player.bot1 = self.Bot4
    	    	        self.player.bot2 = self.Bot5
    	    	        self.player.bot3 = self.Bot3
    	    	        self.player.bot4 = self.Bot1
    	    	        self.player.bot5 = self.Bot2
    	    	        BattleResultMessage(self.client, self.player).send(crypter)
            else:
    	    	    if self.player.team == 0:

    	    	        self.player.bot1_n = self.Bot1N
    	    	        self.player.bot2_n = self.Bot2N
    	    	        self.player.bot3_n = self.Bot3N
    	    	        self.player.bot4_n = self.Bot4N
    	    	        self.player.bot5_n = self.Bot5N
    	    	        self.player.bot1 = self.Bot1
    	    	        self.player.bot2 = self.Bot2
    	    	        self.player.bot3 = self.Bot3
    	    	        self.player.bot4 = self.Bot4
    	    	        self.player.bot5 = self.Bot5

    	    	        BattleResultMessage(self.client, self.player).send(crypter)
    	    	    else:

    	    	        self.player.bot1_n = self.Bot4N
    	    	        self.player.bot2_n = self.Bot5N
    	    	        self.player.bot3_n = self.Bot3N
    	    	        self.player.bot4_n = self.Bot1N
    	    	        self.player.bot5_n = self.Bot2N
    	    	        self.player.bot1 = self.Bot4
    	    	        self.player.bot2 = self.Bot5
    	    	        self.player.bot3 = self.Bot3
    	    	        self.player.bot4 = self.Bot1
    	    	        self.player.bot5 = self.Bot2
    	    	        BattleResultMessage(self.client, self.player).send(crypter)