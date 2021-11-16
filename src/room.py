from commands import Direction

class Room:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

        # Links indexed off of commands.Direction
        self.links = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

    def N(self, roomId):
        self.links[Direction.N] = roomId

    def NE(self, roomId):
        self.links[Direction.NE] = roomId

    def E(self, roomId):
        self.links[Direction.E] = roomId

    def SE(self, roomId):
        self.links[Direction.SE] = roomId

    def S(self, roomId):
        self.links[Direction.S] = roomId

    def SW(self, roomId):
        self.links[Direction.SW] = roomId

    def W(self, roomId):
        self.links[Direction.W] = roomId

    def NW(self, roomId):
        self.links[Direction.NW] = roomId

    def U(self, roomId):
        self.links[Direction.U] = roomId

    def D(self, roomId):
        self.links[Direction.D] = roomId

