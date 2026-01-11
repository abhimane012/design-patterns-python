# Game Factory

from abc import ABC, abstractmethod


class GameObject(ABC):
    @abstractmethod
    def display(self):
        pass


############ Character #############
class Character(GameObject):
    @abstractmethod
    def display(self):
        pass


class Soldier(Character):
    def display(self):
        print(f"Character: {self.__class__.__name__}")


class Warrior(Character):
    def display(self):
        print(f"Character: {self.__class__.__name__}")


class SuperSoldier(Character):
    def display(self):
        print(f"Character: {self.__class__.__name__}")


############ Weapon ###############
class Weapon(GameObject):
    @abstractmethod
    def display(self):
        pass


class AK47(Weapon):
    def display(self):
        print(f"Weapon: {self.__class__.__name__}")


class Katana(Weapon):
    def display(self):
        print(f"Weapon: {self.__class__.__name__}")


class Sniper(Weapon):
    def display(self):
        print(f"Weapon: {self.__class__.__name__}")


############ Level ################
class GameLevel(GameObject):
    @abstractmethod
    def display(self):
        pass


class Easy(GameLevel):
    def display(self):
        print(f"Game Level: {self.__class__.__name__}")


class Medium(GameLevel):
    def display(self):
        print(f"Game Level: {self.__class__.__name__}")


class Hard(GameLevel):
    def display(self):
        print(f"Game Level: {self.__class__.__name__}")


######## GameFactory ##########
class GameFactory(ABC):
    @abstractmethod
    def create_charater(self):
        pass

    @abstractmethod
    def create_weapon(self):
        pass

    @abstractmethod
    def create_game_level(self):
        pass


class BasicGameFactory(GameFactory):
    def create_charater(self):
        return Soldier()

    def create_weapon(self):
        return AK47()

    def create_game_level(self):
        return Easy()


class AmatureGameFactory(GameFactory):
    def create_charater(self):
        return Warrior()

    def create_weapon(self):
        return Katana()

    def create_game_level(self):
        return Medium()


class ProfessionalGameFactory(GameFactory):
    def create_charater(self):
        return SuperSoldier()

    def create_weapon(self):
        return Sniper()

    def create_game_level(self):
        return Hard()


#### Client Code


class Client:
    def __init__(self):
        self.factory = dict(
            basic=BasicGameFactory,
            amature=AmatureGameFactory,
            pro=ProfessionalGameFactory,
        )

    def get_game_factory(self, game_type):
        if game_type in self.factory:
            return self.factory.get(game_type)()


if __name__ == "__main__":
    game_client = Client()

    game = game_client.get_game_factory("basic")
    game.create_charater().display()
    game.create_weapon().display()
    game.create_game_level().display()

    print()

    game = game_client.get_game_factory("amature")
    game.create_charater().display()
    game.create_weapon().display()
    game.create_game_level().display()

    print()

    game = game_client.get_game_factory("pro")
    game.create_charater().display()
    game.create_weapon().display()
    game.create_game_level().display()
