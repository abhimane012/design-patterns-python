# Flyweight Pattern


class Flyweight:
    def __init__(self, state):
        self.state = state


class FlyweightCreator:
    _created = 0
    _flyweights = dict()

    @staticmethod
    def get_flyweight(state):
        if state in FlyweightCreator._flyweights:
            return FlyweightCreator._flyweights.get(state)
        else:
            FlyweightCreator._flyweights[state] = Flyweight(state)
            FlyweightCreator._created += 1
            return FlyweightCreator._flyweights.get(state)


if __name__ == "__main__":
    objs = [
        FlyweightCreator.get_flyweight(1),
        FlyweightCreator.get_flyweight(1),
        FlyweightCreator.get_flyweight(1),
        FlyweightCreator.get_flyweight(2),
        FlyweightCreator.get_flyweight(2),
        FlyweightCreator.get_flyweight(2),
        FlyweightCreator.get_flyweight(2),
        FlyweightCreator.get_flyweight(3),
        FlyweightCreator.get_flyweight(3),
        FlyweightCreator.get_flyweight(3),
        FlyweightCreator.get_flyweight(3),
        FlyweightCreator.get_flyweight(3),
        FlyweightCreator.get_flyweight(4),
        FlyweightCreator.get_flyweight(4),
        FlyweightCreator.get_flyweight(4),
        FlyweightCreator.get_flyweight(5),
        FlyweightCreator.get_flyweight(6),
        FlyweightCreator.get_flyweight(7),
        FlyweightCreator.get_flyweight(8),
        FlyweightCreator.get_flyweight(1),
        FlyweightCreator.get_flyweight(1),
        FlyweightCreator.get_flyweight(1),
        FlyweightCreator.get_flyweight(1),
        FlyweightCreator.get_flyweight(1),
        FlyweightCreator.get_flyweight(9),
    ]

    print(f"Flyweights created {FlyweightCreator._created}")
