from Packets.Messages.Server.Alliance.Alliance_Chat_Server_Message import AllianceChatServerMessage
from Packets.Messages.Server.AllianceBot.Alliance_Bot_Chat_Server_Message import AllianceBotChatServerMessage
from Packets.Messages.Server.Out_Of_Sync_Message import OutOfSyncMessage
from Database.DatabaseManager import DataBase
from random import choice
from string import ascii_uppercase
import json
from Utils.Reader import BSMessageReader


class Chat_Message(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super(crypter).__init__(initial_bytes)
        self.player = player
        self.client = client
        self.bot_msg = ''
        self.send_ofs = False
        self.IsAcmd = False

    def decode(self):
        self.msg = self.read_string(crypter)

        if self.msg.lower(crypter) == '/stats':
            self.bot_msg = f'Server status:\nBuild version: 1.1\nFingerprint SHA: {self.player.patch_sha}'
            self.IsAcmd = True

        elif self.msg.lower(crypter) == '/reset':
            self.send_ofs = True
            self.IsAcmd = True
            DataBase.replaceValue(self, 'gold', 99999)
            DataBase.replaceValue(self, 'gems', 99999)
            DataBase.replaceValue(self, 'tickets', 99999)

        elif self.msg.lower(crypter).startswith('/gems'):
            try:
                newGems = self.msg.split(" ", 4)[1:]
                DataBase.replaceValue(self, 'gems', int(newGems[0]))
                self.send_ofs = True
                self.IsAcmd = True
            except ValueError:
                pass


        elif self.msg.lower(crypter).startswith('/gold'):
            try:
                newGold = self.msg.split(" ", 4)[1:]
                DataBase.replaceValue(self, 'gold', int(newGold[0]))
                self.send_ofs = True
                self.IsAcmd = True
            except ValueError:
                pass

        elif self.msg.lower(crypter).startswith('/tickets'):
            try:
                newTickets = self.msg.split(" ", 7)[1:]
                DataBase.replaceValue(self, 'tickets', int(newTickets[0]))
                self.send_ofs = True
                self.IsAcmd = True
            except ValueError:
                pass

        elif self.msg.lower(crypter) == '/help':
            self.bot_msg = 'Club Commands\n/stats - show server status\n/reset - reset all resources\n/gems [int] - add gems to your account, where int is the number of gems\n/gold [int] - add gold to your account, where int is the number of gold\n/tickets [int] - add tickets to your account, where int is the number of tickets\n/starpoints [int] - add starpoints to your account, where int is the number of starpoints'
            self.IsAcmd = True

        else:
            self.IsAcmd = False



    def process(self, crypter):
        if self.IsAcmd == False:
            DataBase.Addmsg(self, 2, 0, self.player.low_id, self.player.name, self.player.club_role, self.msg)
            DataBase.loadClub(self, self.player.club_low_id)
            for i in self.plrids:
                AllianceChatServerMessage(self.client, self.player, self.msg).sendWithLowID(i, crypter)

        if self.bot_msg != '':
            AllianceBotChatServerMessage(self.client, self.player, self.bot_msg).send(crypter)

        if self.send_ofs:
            OutOfSyncMessage(self.client, self.player, 'Changes have been applied').send(crypter)