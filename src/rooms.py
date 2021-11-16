#!/usr/bin/env python3

import environment
import engine
import parser

def commandloop():
    while True:
        print()

        commandInput = input("> ")
        command = parser.parseCommand(commandInput)

        print()

        if not engine.processCommand(command):
            break
    

def main():
    global env
    global engine

    env = environment.Environment()
    engine = engine.Engine(env)

    print()
    engine.look(None)

    commandloop()

    env.save()


if __name__ == "__main__":
    
    main()

print()
print("Your room has disolved into nothingness and you blink out of existence.")
print()