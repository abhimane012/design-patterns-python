# Game Engine Prototype
import copy


class GameObject:
    def __init__(self, name: str):
        self.name = name

    def clone(self):
        return copy.deepcopy(self)


class Player(GameObject):
    def __init__(self, name: str, health: int):
        super().__init__(name)
        self.health = health


class Enemy(GameObject):
    def __init__(self, name: str, health: int):
        super().__init__(name)
        self.strength = health


class GameEngine:
    def __init__(self):
        self.game_prototypes = dict()

    def register_prototype(self, key, obj):
        self.game_prototypes[key] = obj

    def create_object(self, key):
        proto = self.game_prototypes.get(key)
        if proto:
            return proto.clone()


if __name__ == "__main__":
    game_engine = GameEngine()

    player1 = Player("Normal Player", 100)
    enemy1 = Enemy("Normal Enemy", 120)

    game_engine.register_prototype("player", player1)
    game_engine.register_prototype("enemy", enemy1)

    player2 = game_engine.create_object("player")
    player2.name = "Pro Player"
    player2.health = 150

    enemy2 = game_engine.create_object("enemy")
    enemy2.name = "Pro Enemy"
    enemy2.strength = 200
