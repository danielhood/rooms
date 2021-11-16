#!/usr/bin/env python3

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
    else:
        print ("You look around, somewhat confused.")

    return False

def commandloop():
    exitGame = False
    while not exitGame:
        commandInput = input("> ")
        exitGame = parseCommand(commandInput)
    

def main():
    print("You are in a room.")
    commandloop()



if __name__ == "__main__":
    main()

print("Your room has disolved into nothingness and you blink out of existence.")