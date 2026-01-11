class GameState:
    def __init__(self, level, score):
        self.level = level
        self.score = score

    def get_level(self):
        return self.level

    def get_score(self):
        return self.score


class CareTaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]


class Game:
    def __init__(self):
        self.level = 1
        self.score = 0

    def next_level(self):
        self.level += 1

    def add_score(self, val):
        self.score += val

    def save_game_state(self):
        return GameState(self.level, self.score)

    def restore_game_state(self, memento):
        self.level = memento.get_level()
        self.score = memento.get_score()


if __name__ == "__main__":
    game = Game()
    caretaker = CareTaker()

    game.next_level()
    game.add_score(20)

    print(f"Level - {game.level} and Score - {game.score}")

    caretaker.add_memento(game.save_game_state())

    game.next_level()
    game.add_score(20)

    print(f"Level - {game.level} and Score - {game.score}")

    caretaker.add_memento(game.save_game_state())

    game.restore_game_state(caretaker.get_memento(0))

    print(f"Level - {game.level} and Score - {game.score}")
