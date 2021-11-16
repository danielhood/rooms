class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.room = 0

    def setRoom(self, roomId):
        self.room = roomId
