from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class BattleResultDuoShowdownMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):
        self.writeVint(5) # Battle Result Type
        self.writeVint(self.player.rank) # Rank Score

        brawler_trophies = self.player.brawlers_trophies[str(self.player.brawler_id)]
        brawler_trophies_for_rank = self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)]
        brawler_level = self.player.Brawler_level[str(self.player.brawler_id)] + 1
        exp_reward = [14, 8, 4, 2, 0]
        token_list = [32, 20, 8, 4, 0]
        practice_exp_reward = [7, 4, 2, 1, 0] # Might be Wrong idk
        practice_token_list = [16, 10, 4, 2, 0] # Might be Wrong idk
        if 1 <= self.player.rank <= 2:
            result = self.player.result + 1
        if self.player.rank >= 3:
            result = self.player.result

        if 0 <= brawler_trophies <= 29:
            rank_1_val = 7
            rank_2_val = 5
            rank_3_val = 4
            rank_4_val = 2
            rank_5_val = 0

            rank_1_val2 = 7
            rank_2_val2 = 5
            rank_3_val2 = 4
            rank_4_val2 = 2
            rank_5_val2 = 0

        else:
            if 30 <= brawler_trophies <= 59:
                rank_1_val = 7
                rank_2_val = 5
                rank_3_val = 2
                rank_4_val = -1
                rank_5_val = -3

                rank_1_val2 = 7
                rank_2_val2 = 5
                rank_3_val2 = 2
                rank_4_val2 = -64
                rank_5_val2 = -62

            if 60 <= brawler_trophies <= 99:
                rank_1_val = 7
                rank_2_val = 4
                rank_3_val = 2
                rank_4_val = -1
                rank_5_val = -4

                rank_1_val2 = 7
                rank_2_val2 = 4
                rank_3_val2 = 2
                rank_4_val2 = -64
                rank_5_val2 = -61

            if 100 <= brawler_trophies <= 139:
                rank_1_val = 6
                rank_2_val = 4
                rank_3_val = 1
                rank_4_val = -1
                rank_5_val = -4

                rank_1_val2 = 6
                rank_2_val2 = 4
                rank_3_val2 = 1
                rank_4_val2 = -64
                rank_5_val2 = -61

            if 140 <= brawler_trophies <= 219:
                rank_1_val = 6
                rank_2_val = 4
                rank_3_val = 1
                rank_4_val = -2
                rank_5_val = -5

                rank_1_val2 = 6
                rank_2_val2 = 4
                rank_3_val2 = 1
                rank_4_val2 = -63
                rank_5_val2 = -60

            if 220 <= brawler_trophies <= 499:
                rank_1_val = 6
                rank_2_val = 3
                rank_3_val = 0
                rank_4_val = -3
                rank_5_val = -6

                rank_1_val2 = 6
                rank_2_val2 = 3
                rank_3_val2 = 0
                rank_4_val2 = -62
                rank_5_val2 = -59

            if 500 <= brawler_trophies <= 599:
                rank_1_val = 6
                rank_2_val = 3
                rank_3_val = 0
                rank_4_val = -4
                rank_5_val = -6

                rank_1_val2 = 6
                rank_2_val2 = 3
                rank_3_val2 = 0
                rank_4_val2 = -61
                rank_5_val2 = -59

            if 600 <= brawler_trophies <= 699:
                rank_1_val = 4
                rank_2_val = 2
                rank_3_val = -1
                rank_4_val = -4
                rank_5_val = -6

                rank_1_val2 = 4
                rank_2_val2 = 2
                rank_3_val2 = -64
                rank_4_val2 = -61
                rank_5_val2 = -59

            if 700 <= brawler_trophies <= 799:
                rank_1_val = 3
                rank_2_val = 1
                rank_3_val = -1
                rank_4_val = -4
                rank_5_val = -6

                rank_1_val2 = 3
                rank_2_val2 = 1
                rank_3_val2 = -64
                rank_4_val2 = -61
                rank_5_val2 = -59

            if 800 <= brawler_trophies <= 899:
                rank_1_val = 3
                rank_2_val = 1
                rank_3_val = -2
                rank_4_val = -5
                rank_5_val = -7

                rank_1_val2 = 3
                rank_2_val2 = 1
                rank_3_val2 = -63
                rank_4_val2 = -60
                rank_5_val2 = -58

            if brawler_trophies >= 900:
                rank_1_val = 2
                rank_2_val = 0
                rank_3_val = -3
                rank_4_val = -5
                rank_5_val = -7

                rank_1_val2 = 2
                rank_2_val2 = 0
                rank_3_val2 = -62
                rank_4_val2 = -60
                rank_5_val2 = -58

        if self.player.rank == 1:
            trophiesinresult = rank_1_val2
            if result == 0:
                trophies = 0
                experience = practice_exp_reward[0]
                tokens = practice_token_list[0]
                startoken = 0
            if result == 1:
                trophies = 0
                experience = practice_exp_reward[0]
                tokens = practice_token_list[0]
                startoken = 1
            if result == 2:
                trophies = 0
                experience = 0
                tokens = practice_token_list[0]
                startoken = 0
            if result == 3:
                trophies = 0
                experience = 0
                tokens = practice_token_list[0]
                startoken = 1
            if result == 4:
                trophies = 0
                experience = practice_exp_reward[0]
                tokens = 0
                startoken = 0
            if result == 5:
                trophies = 0
                experience = practice_exp_reward[0]
                tokens = 0
                startoken = 1
            if result == 6:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 7:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 1
            if result == 8:
                trophies = 0
                experience = practice_exp_reward[0]
                tokens = practice_token_list[0]
                startoken = 0
            if result == 9:
                trophies = 0
                experience = practice_exp_reward[0]
                tokens = practice_token_list[0]
                startoken = 1
            if result == 10:
                trophies = 0
                experience = 0
                tokens = practice_token_list[0]
                startoken = 0
            if result == 11:
                trophies = 0
                experience = 0
                tokens = practice_token_list[0]
                startoken = 1
            if result == 12:
                trophies = 0
                experience = practice_exp_reward[0]
                tokens = 0
                startoken = 0
            if result == 13:
                trophies = 0
                experience = practice_exp_reward[0]
                tokens = 0
                startoken = 1
            if result == 14:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 15:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 1
            if result == 16:
                trophies = rank_1_val
                experience = exp_reward[0]
                tokens = token_list[0]
                startoken = 0
            if result == 17:
                trophies = rank_1_val
                experience = exp_reward[0]
                tokens = token_list[0]
                startoken = 1
            if result == 18:
                trophies = rank_1_val
                experience = 0
                tokens = token_list[0]
                startoken = 0
            if result == 19:
                trophies = rank_1_val
                experience = 0
                tokens = token_list[0]
                startoken = 1
            if result == 20:
                trophies = rank_1_val
                experience = exp_reward[0]
                tokens = 0
                startoken = 0
            if result == 21:
                trophies = rank_1_val
                experience = exp_reward[0]
                tokens = 0
                startoken = 1
            if result == 22:
                trophies = rank_1_val
                experience = 0
                tokens = 0
                startoken = 0
            if result == 23:
                trophies = rank_1_val
                experience = 0
                tokens = 0
                startoken = 1
            if result == 24:
                trophies = rank_1_val
                experience = exp_reward[0]
                tokens = token_list[0]
                startoken = 0
            if result == 25:
                trophies = rank_1_val
                experience = exp_reward[0]
                tokens = token_list[0]
                startoken = 1
            if result == 26:
                trophies = rank_1_val
                experience = 0
                tokens = token_list[0]
                startoken = 0
            if result == 27:
                trophies = rank_1_val
                experience = 0
                tokens = token_list[0]
                startoken = 1
            if result == 28:
                trophies = rank_1_val
                experience = exp_reward[0]
                tokens = 0
                startoken = 0
            if result == 29:
                trophies = rank_1_val
                experience = exp_reward[0]
                tokens = 0
                startoken = 1
            if result == 30:
                trophies = rank_1_val
                experience = 0
                tokens = 0
                startoken = 0
            if result == 31:
                trophies = rank_1_val
                experience = 0
                tokens = 0
                startoken = 1
                
            self.player.duo_wins += 1
            self.player.player_experience += experience
            if self.player.tokensdoubler <= 0:
                doubledtokens = 0
            if self.player.tokensdoubler > tokens:
                doubledtokens = tokens
            if tokens > self.player.tokensdoubler: 
                doubledtokens = self.player.tokensdoubler
            remainingtokens = (self.player.tokensdoubler) - doubledtokens
            totaltokens = tokens + doubledtokens
            new_trophies = self.player.trophies + trophies
            new_tokens = self.player.brawl_boxes + totaltokens
            new_startokens = self.player.big_boxes + startoken
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + trophies
            if self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] < self.player.brawlers_trophies[str(self.player.brawler_id)]:
                self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + trophies
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            DataBase.replaceValue(self, 'bigBoxes', new_startokens)
            DataBase.replaceValue(self, 'tokensdoubler', remainingtokens)
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)
            DataBase.replaceValue(self, 'duoWins', self.player.duo_wins)
            
        if self.player.rank == 2:
            trophiesinresult = rank_2_val2
            if result == 0:
                trophies = 0
                experience = practice_exp_reward[1]
                tokens = practice_token_list[1]
                startoken = 0
            if result == 1:
                trophies = 0
                experience = practice_exp_reward[1]
                tokens = practice_token_list[1]
                startoken = 1
            if result == 2:
                trophies = 0
                experience = 0
                tokens = practice_token_list[1]
                startoken = 0
            if result == 3:
                trophies = 0
                experience = 0
                tokens = practice_token_list[1]
                startoken = 1
            if result == 4:
                trophies = 0
                experience = practice_exp_reward[1]
                tokens = 0
                startoken = 0
            if result == 5:
                trophies = 0
                experience = practice_exp_reward[1]
                tokens = 0
                startoken = 1
            if result == 6:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 7:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 1
            if result == 8:
                trophies = 0
                experience = practice_exp_reward[1]
                tokens = practice_token_list[1]
                startoken = 0
            if result == 9:
                trophies = 0
                experience = practice_exp_reward[1]
                tokens = practice_token_list[1]
                startoken = 1
            if result == 10:
                trophies = 0
                experience = 0
                tokens = practice_token_list[1]
                startoken = 0
            if result == 11:
                trophies = 0
                experience = 0
                tokens = practice_token_list[1]
                startoken = 1
            if result == 12:
                trophies = 0
                experience = practice_exp_reward[1]
                tokens = 0
                startoken = 0
            if result == 13:
                trophies = 0
                experience = practice_exp_reward[1]
                tokens = 0
                startoken = 1
            if result == 14:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 15:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 1
            if result == 16:
                trophies = rank_2_val
                experience = exp_reward[1]
                tokens = token_list[1]
                startoken = 0
            if result == 17:
                trophies = rank_2_val
                experience = exp_reward[1]
                tokens = token_list[1]
                startoken = 1
            if result == 18:
                trophies = rank_2_val
                experience = 0
                tokens = token_list[1]
                startoken = 0
            if result == 19:
                trophies = rank_2_val
                experience = 0
                tokens = token_list[1]
                startoken = 1
            if result == 20:
                trophies = rank_2_val
                experience = exp_reward[1]
                tokens = 0
                startoken = 0
            if result == 21:
                trophies = rank_2_val
                experience = exp_reward[1]
                tokens = 0
                startoken = 1
            if result == 22:
                trophies = rank_2_val
                experience = 0
                tokens = 0
                startoken = 0
            if result == 23:
                trophies = rank_2_val
                experience = 0
                tokens = 0
                startoken = 1
            if result == 24:
                trophies = rank_2_val
                experience = exp_reward[1]
                tokens = token_list[1]
                startoken = 0
            if result == 25:
                trophies = rank_2_val
                experience = exp_reward[1]
                tokens = token_list[1]
                startoken = 1
            if result == 26:
                trophies = rank_2_val
                experience = 0
                tokens = token_list[1]
                startoken = 0
            if result == 27:
                trophies = rank_2_val
                experience = 0
                tokens = token_list[1]
                startoken = 1
            if result == 28:
                trophies = rank_2_val
                experience = exp_reward[1]
                tokens = 0
                startoken = 0
            if result == 29:
                trophies = rank_2_val
                experience = exp_reward[1]
                tokens = 0
                startoken = 1
            if result == 30:
                trophies = rank_2_val
                experience = 0
                tokens = 0
                startoken = 0
            if result == 31:
                trophies = rank_2_val
                experience = 0
                tokens = 0
                startoken = 1
                
            self.player.player_experience += experience
            if self.player.tokensdoubler <= 0:
                doubledtokens = 0
            if self.player.tokensdoubler > tokens:
                doubledtokens = tokens
            if tokens > self.player.tokensdoubler: 
                doubledtokens = self.player.tokensdoubler
            remainingtokens = (self.player.tokensdoubler) - doubledtokens
            totaltokens = tokens + doubledtokens
            new_trophies = self.player.trophies + trophies
            new_tokens = self.player.brawl_boxes + totaltokens
            new_startokens = self.player.big_boxes + startoken
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + trophies
            if self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] < self.player.brawlers_trophies[str(self.player.brawler_id)]:
                self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + trophies
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            DataBase.replaceValue(self, 'bigBoxes', new_startokens)
            DataBase.replaceValue(self, 'tokensdoubler', remainingtokens)
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)
            
        if self.player.rank == 3:
            trophiesinresult = rank_3_val2
            startoken = 0
            if result == 0:
                trophies = 0
                experience = practice_exp_reward[2]
                tokens = practice_token_list[2]
            if result == 1:
                trophies = 0
                experience = practice_exp_reward[2]
                tokens = practice_token_list[2]
            if result == 2:
                trophies = 0
                experience = 0
                tokens = practice_token_list[2]
            if result == 3:
                trophies = 0
                experience = 0
                tokens = practice_token_list[2]
            if result == 4:
                trophies = 0
                experience = practice_exp_reward[2]
                tokens = 0
            if result == 5:
                trophies = 0
                experience = practice_exp_reward[2]
                tokens = 0
            if result == 6:
                trophies = 0
                experience = 0
                tokens = 0
            if result == 7:
                trophies = 0
                experience = 0
                tokens = 0
            if result == 8:
                trophies = 0
                experience = practice_exp_reward[2]
                tokens = practice_token_list[2]
            if result == 9:
                trophies = 0
                experience = practice_exp_reward[2]
                tokens = practice_token_list[2]
            if result == 10:
                trophies = 0
                experience = 0
                tokens = practice_token_list[2]
            if result == 11:
                trophies = 0
                experience = 0
                tokens = practice_token_list[2]
            if result == 12:
                trophies = 0
                experience = practice_exp_reward[2]
                tokens = 0
            if result == 13:
                trophies = 0
                experience = practice_exp_reward[2]
                tokens = 0
            if result == 14:
                trophies = 0
                experience = 0
                tokens = 0
            if result == 15:
                trophies = 0
                experience = 0
                tokens = 0
            if result == 16:
                trophies = rank_3_val
                experience = exp_reward[2]
                tokens = token_list[2]
            if result == 17:
                trophies = rank_3_val
                experience = exp_reward[2]
                tokens = token_list[2]
            if result == 18:
                trophies = rank_3_val
                experience = 0
                tokens = token_list[2]
            if result == 19:
                trophies = rank_3_val
                experience = 0
                tokens = token_list[2]
            if result == 20:
                trophies = rank_3_val
                experience = exp_reward[2]
                tokens = 0
            if result == 21:
                trophies = rank_3_val
                experience = exp_reward[2]
                tokens = 0
            if result == 22:
                trophies = rank_3_val
                experience = 0
                tokens = 0
            if result == 23:
                trophies = rank_3_val
                experience = 0
                tokens = 0
            if result == 24:
                trophies = rank_3_val
                experience = exp_reward[2]
                tokens = token_list[2]
            if result == 25:
                trophies = rank_3_val
                experience = exp_reward[2]
                tokens = token_list[2]
            if result == 26:
                trophies = rank_3_val
                experience = 0
                tokens = token_list[2]
            if result == 27:
                trophies = rank_3_val
                experience = 0
                tokens = token_list[2]
            if result == 28:
                trophies = rank_3_val
                experience = exp_reward[2]
                tokens = 0
            if result == 29:
                trophies = rank_3_val
                experience = exp_reward[2]
                tokens = 0
            if result == 30:
                trophies = rank_3_val
                experience = 0
                tokens = 0
            if result == 31:
                trophies = rank_3_val
                experience = 0
                tokens = 0
                
            self.player.player_experience += experience
            if self.player.tokensdoubler <= 0:
                doubledtokens = 0
            if self.player.tokensdoubler > tokens:
                doubledtokens = tokens
            if tokens > self.player.tokensdoubler: 
                doubledtokens = self.player.tokensdoubler
            remainingtokens = (self.player.tokensdoubler) - doubledtokens
            totaltokens = tokens + doubledtokens
            new_trophies = self.player.trophies + trophies
            new_tokens = self.player.brawl_boxes + totaltokens
            new_startokens = self.player.big_boxes + startoken
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + trophies
            if self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] < self.player.brawlers_trophies[str(self.player.brawler_id)]:
                self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + trophies
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            DataBase.replaceValue(self, 'bigBoxes', new_startokens)
            DataBase.replaceValue(self, 'tokensdoubler', remainingtokens)
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)
            
        if self.player.rank == 4:
            trophiesinresult = rank_4_val2
            startoken = 0
            if result == 0:
                trophies = 0
                experience = practice_exp_reward[3]
                tokens = practice_token_list[3]
            if result == 1:
                trophies = 0
                experience = practice_exp_reward[3]
                tokens = practice_token_list[3]
            if result == 2:
                trophies = 0
                experience = 0
                tokens = practice_token_list[3]
            if result == 3:
                trophies = 0
                experience = 0
                tokens = practice_token_list[3]
            if result == 4:
                trophies = 0
                experience = practice_exp_reward[3]
                tokens = 0
            if result == 5:
                trophies = 0
                experience = practice_exp_reward[3]
                tokens = 0
            if result == 6:
                trophies = 0
                experience = 0
                tokens = 0
            if result == 7:
                trophies = 0
                experience = 0
                tokens = 0
            if result == 8:
                trophies = 0
                experience = practice_exp_reward[3]
                tokens = practice_token_list[3]
            if result == 9:
                trophies = 0
                experience = practice_exp_reward[3]
                tokens = practice_token_list[3]
            if result == 10:
                trophies = 0
                experience = 0
                tokens = practice_token_list[3]
            if result == 11:
                trophies = 0
                experience = 0
                tokens = practice_token_list[3]
            if result == 12:
                trophies = 0
                experience = practice_exp_reward[3]
                tokens = 0
            if result == 13:
                trophies = 0
                experience = practice_exp_reward[3]
                tokens = 0
            if result == 14:
                trophies = 0
                experience = 0
                tokens = 0
            if result == 15:
                trophies = 0
                experience = 0
                tokens = 0
            if result == 16:
                trophies = rank_4_val
                experience = exp_reward[3]
                tokens = token_list[3]
            if result == 17:
                trophies = rank_4_val
                experience = exp_reward[3]
                tokens = token_list[3]
            if result == 18:
                trophies = rank_4_val
                experience = 0
                tokens = token_list[3]
            if result == 19:
                trophies = rank_4_val
                experience = 0
                tokens = token_list[3]
            if result == 20:
                trophies = rank_4_val
                experience = exp_reward[3]
                tokens = 0
            if result == 21:
                trophies = rank_4_val
                experience = exp_reward[3]
                tokens = 0
            if result == 22:
                trophies = rank_4_val
                experience = 0
                tokens = 0
            if result == 23:
                trophies = rank_4_val
                experience = 0
                tokens = 0
            if result == 24:
                trophies = rank_4_val
                experience = exp_reward[3]
                tokens = token_list[3]
            if result == 25:
                trophies = rank_4_val
                experience = exp_reward[3]
                tokens = token_list[3]
            if result == 26:
                trophies = rank_4_val
                experience = 0
                tokens = token_list[3]
            if result == 27:
                trophies = rank_4_val
                experience = 0
                tokens = token_list[3]
            if result == 28:
                trophies = rank_4_val
                experience = exp_reward[3]
                tokens = 0
            if result == 29:
                trophies = rank_4_val
                experience = exp_reward[3]
                tokens = 0
            if result == 30:
                trophies = rank_4_val
                experience = 0
                tokens = 0
            if result == 31:
                trophies = rank_4_val
                experience = 0
                tokens = 0
                
            self.player.player_experience += experience
            if self.player.tokensdoubler <= 0:
                doubledtokens = 0
            if self.player.tokensdoubler > tokens:
                doubledtokens = tokens
            if tokens > self.player.tokensdoubler: 
                doubledtokens = self.player.tokensdoubler
            remainingtokens = (self.player.tokensdoubler) - doubledtokens
            totaltokens = tokens + doubledtokens
            new_trophies = self.player.trophies + trophies
            new_tokens = self.player.brawl_boxes + totaltokens
            new_startokens = self.player.big_boxes + startoken
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + trophies
            if self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] < self.player.brawlers_trophies[str(self.player.brawler_id)]:
                self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + trophies
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            DataBase.replaceValue(self, 'bigBoxes', new_startokens)
            DataBase.replaceValue(self, 'tokensdoubler', remainingtokens)
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)
                  
        if self.player.rank == 5:
            startoken = 0
            experience = 0
            tokens = 0
            trophiesinresult = rank_5_val2
            if 0 <= result <= 15:
                trophies = 0
            if 16 <= result <= 31:
                trophies = rank_5_val
            
            if self.player.tokensdoubler <= 0:
                doubledtokens = 0
            if self.player.tokensdoubler > tokens:
                doubledtokens = tokens
            if tokens > self.player.tokensdoubler: 
                doubledtokens = self.player.tokensdoubler
            remainingtokens = (self.player.tokensdoubler) - doubledtokens
            totaltokens = tokens + doubledtokens  
            new_trophies = self.player.trophies + trophies
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + trophies
            if self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] < self.player.brawlers_trophies[str(self.player.brawler_id)]:
                self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + trophies
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'trophies', new_trophies)

        self.writeVint(tokens) # Tokens Gained
        if self.player.result < 16:
            self.writeVint(0) # Trophies Result 
        if self.player.result >= 16:
            self.writeVint(trophiesinresult) # Trophies Result
        self.writeVint(doubledtokens) # Doubled Tokens
        self.writeVint(remainingtokens) # Token Doubler Remaining
        self.writeVint(0) # Unknown
        self.writeVint(result) # Battle Result Info and Stuff
        self.writeVint(2) # Battle End Screen Players
        
        self.writeString(self.player.name) # Your Name
        self.writeVint(1) # Self Star Player Type
        self.writeVint(16) # Player Brawler 
        self.writeVint(self.player.brawler_id)
        self.writeVint(29) # Player Skin 
        self.writeVint(self.player.skin_id)
        self.writeVint(brawler_trophies) # Your Brawler Trophies
        self.writeVint(10) # Your Brawler Power Level
        bool = True
        self.writeBoolean(bool)
        if bool == True:
            self.writeInt(0) # Your HighID
            self.writeInt(1) # Your LowID
        
        self.writeString('Bot 1') # Bot 1 Name
        self.writeVint(0) # Star Player Type
        self.writeVint(16) # Brawler CsvID
        self.writeVint(self.player.bot1) # Bot 1
        self.writeVint(0) # Skin CsvID
        self.writeVint(0) # Brawler Trophies
        self.writeVint(10) # Brawler Power Level
        bool = True
        self.writeBoolean(bool)
        if bool == True:
            self.writeInt(0) # HighID
            self.writeInt(2) # LowID
        

        # Experience Array
        self.writeVint(2) # Count
        self.writeVint(0) # Normal Experience ID
        self.writeVint(experience) # Normal Experience Ammount
        self.writeVint(8) # Star Player Experience ID
        self.writeVint(0) # Star Player Experience Ammount

        # Rank Up and Level Up Bonus Array
        self.writeVint(0) # Count


        # Trophies and Experience Bars Array
        self.writeVint(2) # Count
        self.writeVint(1) # Ranks Milestone ID
        self.writeVint(brawler_trophies) # Brawler Trophies Bar
        self.writeVint(brawler_trophies_for_rank) # Brawler Trophies for Rank
        self.writeVint(5) # Experience Milestone ID
        self.writeVint(self.player.player_experience -experience) # Total Experience Bar
        self.writeVint(self.player.player_experience -experience) # ???
        
        self.writeScId(26, self.player.profile_icon)  # Player Profile Icon (Unused since 2017)
        self.writeBoolean(True)  # Play Again

        
