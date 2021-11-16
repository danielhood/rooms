import commands

def parseDirection(direction) -> commands.Direction:
    d = direction.lower()
    if d == 'north':
        return commands.Direction.N
    elif d == 'n':
        return commands.Direction.N
    elif d == 'south':
        return commands.Direction.S
    elif d == 's':
        return commands.Direction.S
    elif d == 'east':
        return commands.Direction.E
    elif d == 'e':
        return commands.Direction.E
    elif d == 'west':
        return commands.Direction.W
    elif d == 'w':
        return commands.Direction.W
    elif d == 'northeast':
        return commands.Direction.NE
    elif d == 'ne':
        return commands.Direction.NE
    elif d == 'northwest':
        return commands.Direction.NW
    elif d == 'nw':
        return commands.Direction.NW
    elif d == 'southeast':
        return commands.Direction.SE
    elif d == 'se':
        return commands.Direction.SE
    elif d == 'southwest':
        return commands.Direction.SW
    elif d == 'sw':
        return commands.Direction.SW
    elif d == 'up':
        return commands.Direction.U
    elif d == 'down':
        return commands.Direction.D
    else:
        return None


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
    elif c == 'up':
        return commands.Command(commands.CommandType.MOVE, commands.Direction.U)
    elif c == 'down':
        return commands.Command(commands.CommandType.MOVE, commands.Direction.D)
    elif c.startswith('look'):
        return commands.Command(commands.CommandType.LOOK, parseDirection(c.partition("look ")[2]))
    elif c.startswith('look at'):
        return commands.Command(commands.CommandType.LOOKAT, None, c.partition("look at ")[2])
    elif c.startswith('take'):
        return commands.Command(commands.CommandType.TAKE, None, c.partition("take ")[2])
    elif c.startswith('drop'):
        return commands.Command(commands.CommandType.DROP, None, c.partition("drop ")[2])


    else:
        return commands.Command(commands.CommandType.NONE)
