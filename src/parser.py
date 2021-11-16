import commands

def parseCommand(commandInput) -> commands.Command:
    c = commandInput.lower()
    if c == 'exit':
        return commands.Command(commands.CommandType.EXIT)
    elif c == 'quit':
        return commands.Command(commands.CommandType.EXIT)
    elif c == 'help':
        return commands.Command(commands.CommandType.HELP)
    elif c == 'north':
        return commands.Command(commands.CommandType.MOVE, commands.Direction.N)
    elif c == 'n':
        return commands.Command(commands.CommandType.MOVE, commands.Direction.N)
    elif c == 'south':
        return commands.Command(commands.CommandType.MOVE, commands.Direction.S)
    elif c == 's':
        return commands.Command(commands.CommandType.MOVE, commands.Direction.S)
    elif c == 'east':
        return commands.Command(commands.CommandType.MOVE, commands.Direction.E)
    elif c == 'e':
        return commands.Command(commands.CommandType.MOVE, commands.Direction.E)
    elif c == 'west':
        return commands.Command(commands.CommandType.MOVE, commands.Direction.W)
    elif c == 'w':
        return commands.Command(commands.CommandType.MOVE, commands.Direction.W)
    elif c == 'northeast':
        return commands.Command(commands.CommandType.MOVE, commands.Direction.NE)
    elif c == 'ne':
        return commands.Command(commands.CommandType.MOVE, commands.Direction.NE)
    elif c == 'northwest':
        return commands.Command(commands.CommandType.MOVE, commands.Direction.NW)
    elif c == 'nw':
        return commands.Command(commands.CommandType.MOVE, commands.Direction.NW)
    elif c == 'southeast':
        return commands.Command(commands.CommandType.MOVE, commands.Direction.SE)
    elif c == 'se':
        return commands.Command(commands.CommandType.MOVE, commands.Direction.SE)
    elif c == 'southwest':
        return commands.Command(commands.CommandType.MOVE, commands.Direction.SW)
    elif c == 'sw':
        return commands.Command(commands.CommandType.MOVE, commands.Direction.SW)

    else:
        return commands.Command(commands.CommandType.NONE)
