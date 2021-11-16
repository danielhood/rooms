import commands

class Engine:
    def __init__(self, environment):
        self.env = environment

    def processCommand(self, command) -> bool:
        if command.commandType == commands.CommandType.HELP:
            self.showHelp()
        elif command.commandType == commands.CommandType.EXIT:
            return False
        elif command.commandType == commands.CommandType.NONE:
            print ("You look around, somewhat confused.")
        elif command.commandType == commands.CommandType.MOVE:
            self.move(command.direction)
        elif command.commandType == commands.CommandType.LOOK:
            self.look(command.direction)
        elif command.commandType == commands.CommandType.LOOKAT:
            self.lookat(command.target)
        elif command.commandType == commands.CommandType.TAKE:
            self.take(command.target)
        elif command.commandType == commands.CommandType.DROP:
            self.drop(command.target)
        else:
            print ("You blink repeatedly, astonished nothing happend.")
        
        return True

    def move(self, direction):
        newRoom = self.env.world.rooms[self.env.player.room].links[direction]

        if (newRoom == -1):
            print ("You attempt to walk into a wall.")
            return

        self.env.player.room = newRoom

        print (self.env.player.name + " is in room " + self.env.world.rooms[self.env.player.room].name)    

    def look(self, direction):
        if (direction is None):
            print (self.env.world.rooms[self.env.player.room].description)
        else:
            print ("You don't see anything remarkable.")

    def lookat(self, item):
        print (f"You look at the {item}")

    def take(self, item):
        print (f"You take the {item}")

    def drop(self, item):
        print (f"You drop the {item}")

    def showHelp(self):
        print("Commands: help, exit, quit, look [<direction>], look at <object>, bag, inventory")
        print("Movement: north, n, south, s, southwest, sw, left, right, up, down, ...")
        print("Actions (typically <action> <object>): take, drop, eat, wear, lift, push, ...")
