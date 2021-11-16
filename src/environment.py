import player
import world


class Environment:
    def __init__(self):
        self.player = player.Player.load()
        self.world = world.World.load()

    def save(self):
        self.player.save()
        self.world.save()

