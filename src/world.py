import persist
import room

class World:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.rooms = []

    def load():
        temp = persist.load("world")
        if (temp is None):
            temp = World("world0", "A world composed of rooms.")
            temp.initRooms()
            print (f"Created world {temp.name}.")
        else:
            print (f"Loaded world {temp.name}.")

        return temp

    def save(self):
        persist.save("world", self)
        print (f"Saved world {self.name}.")

    def initRooms(self):
        self.rooms = []

        room0 = room.Room(0, "room0", "You are on a stump in the woods.")
        self.rooms.append(room0)

        room1 = room.Room(1, "room1", "You are in a clearing")
        self.rooms.append(room1)

        room0.N(room1.id)
        room1.S(room0.id)

        room2 = room.Room(2, "room2", "You are in a wooded area")
        self.rooms.append(room2)

        room1.N(room2.id)
        room2.S(room1.id)


        room3 = room.Room(3, "room3", "You are in a densely wooded area")
        self.rooms.append(room3)

        room2.N(room3.id)
        room3.S(room2.id)
