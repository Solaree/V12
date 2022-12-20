from Utils.Writer import Writer

class FriendListMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20105
        self.player = player

    def encode(self):
        self.writeInt(1)
        self.writeInt(1)

        self.writeInt(1)
        self.writeInt(1)

        self.writeString("Player")
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeVint(1)
        self.writeVint(10)

        self.writeString()
        self.writeInt(0)

        self.writeVint(0)

        self.writeString()
        self.writeVint(28)
        self.writeVint(11)

        print("[INFO] Message FriendListMessage has been sent.")
