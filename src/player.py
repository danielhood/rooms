import persist

class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.room = 0

    def setRoom(self, roomId):
        self.room = roomId

    def load():
        temp = persist.load("player")
        if (temp is None):
            temp = Player(0, "Player0")
            print (f"Created player {temp.name}.")
        else:
            print (f"Loaded player {temp.name}.")

        return temp


    def save(self):
        persist.save("player", self)
        print (f"Saved player {self.name}.")