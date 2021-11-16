#!/usr/bin/env python3

import environment
import engine
import parser

def commandloop():
    while True:
        commandInput = input("> ")
        command = parser.parseCommand(commandInput)

        if not engine.processCommand(command):
            break
    

def main():
    global env
    global engine

    env = environment.Environment()
    engine = engine.Engine(env)
    
    print("You are in a room.")

    commandloop()

    env.save()


if __name__ == "__main__":
    
    main()

print("Your room has disolved into nothingness and you blink out of existence.")