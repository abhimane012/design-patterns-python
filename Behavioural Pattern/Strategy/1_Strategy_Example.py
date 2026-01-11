from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def operation(self):
        pass


class ConcreteStrategy1(Strategy):
    def operation(self):
        print("Executing Strateg-1............")


class ConcreteStrategy2(Strategy):
    def operation(self):
        print("Executing Strateg-2............")


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_strategy(self):
        self.strategy.operation()


if __name__ == "__main__":
    strategy1 = ConcreteStrategy1()
    strategy2 = ConcreteStrategy2()

    context = Context(strategy1)

    context.execute_strategy()
    context.set_strategy(strategy2)
    context.execute_strategy()
