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
        else:
            print ("You blink repeatedly, astonished nothing happend.")
        
        return True

    def move(self, direction):
        newRoom = self.env.world.rooms[self.env.player.room].links[direction]

        if (newRoom == -1):
            print ("You attempt to walk into a wall")
            return

        self.env.player.room = newRoom

        print (self.env.player.name + " is in room " + self.env.world.rooms[self.env.player.room].name)    

    def showHelp(self):
        print("Commands: help, exit, quit, look, look at <object>, bag, inventory")
        print("Movement: north, n, south, s, southwest, sw, left, right, up, down, ...")
        print("Actions (typically <action> <object>): take, drop, eat, wear, lift, push, ...")
