#!/usr/bin/env python3

import player
import room

def moveNorth():
    if (roomList[p.room].n == -1):
        print ("You attempt to walk into a wall")
        return

    p.room = roomList[p.room].n
    print (str(p.room))
    print (p.name + " is in room " + roomList[p.room].name)    

def moveSouth():
    if (roomList[p.room].s == -1):
        print ("You attempt to walk into a wall")
        return

    p.room = roomList[p.room].s
    print (str(p.room))
    print (p.name + " is in room " + roomList[p.room].name)    



def showHelp():
    print("Commands: help, exit, quit, look, look at <object>, bag, inventory")
    print("Movement: north, n, south, s, southwest, sw, left, right, up, down, ...")
    print("Actions (typically <action> <object>): take, drop, eat, wear, lift, push, ...")


# returns True on exit
def parseCommand(commandInput):
    c = commandInput.lower()
    if c == 'exit':
        return True
    elif c == 'quit':
        return True
    elif c == 'help':
        showHelp()
    elif c == 'north':
        moveNorth()
    elif c == 'n':
        moveNorth()
    elif c == 'south':
        moveSouth()
    elif c == 's':
        moveSouth()

    else:
        print ("You look around, somewhat confused.")

    return False

def commandloop():
    exitGame = False
    while not exitGame:
        commandInput = input("> ")
        exitGame = parseCommand(commandInput)
    

def createPlayer():
    global p
    p = player.Player(0, "Player0")

def createRooms():
    global roomList
    roomList = []
    room0 = room.Room(0, "room0", "You are on a stump in the woods.")
    roomList.append(room0)

    room1 = room.Room(1, "room1", "You are in a clearing")
    roomList.append(room1)

    room2 = room.Room(2, "room2", "You are in a wooded area")
    roomList.append(room2)

    room3 = room.Room(3, "room3", "You are in a densly wooded area")
    roomList.append(room3)

    room0.n = room1.id
    room1.s = room0.id
    room1.n = room2.id
    room2.s = room1.id
    room2.n = room3.id
    room3.s = room2.id



def main():
    createPlayer()
    createRooms()
    print("You are in a room.")
    commandloop()



if __name__ == "__main__":
    
    main()

print("Your room has disolved into nothingness and you blink out of existence.")