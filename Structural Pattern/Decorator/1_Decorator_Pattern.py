# Decorator Pattern
from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class PlainCoffee(Coffee):
    def get_cost(self):
        return 2

    def get_description(self):
        return "Plain Coffee"


class CoffeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

    def get_cost(self):
        return self.coffee.get_cost()

    def get_description(self):
        return self.coffee.get_description()


class Milk(CoffeDecorator):
    def get_cost(self):
        return self.coffee.get_cost() + 1

    def get_description(self):
        return self.coffee.get_description() + "==> Milk "


class Sugar(CoffeDecorator):
    def get_cost(self):
        return self.coffee.get_cost() + 1

    def get_description(self):
        return self.coffee.get_description() + "==> Sugar "


class WhipCream(CoffeDecorator):
    def get_cost(self):
        return self.coffee.get_cost() + 1

    def get_description(self):
        return self.coffee.get_description() + "==> WhipCream "


if __name__ == "__main__":
    plain_coffee = PlainCoffee()
    plain_coffee = Milk(plain_coffee)
    plain_coffee = Sugar(plain_coffee)
    plain_coffee = WhipCream(plain_coffee)

    print(plain_coffee.get_description())
    print(plain_coffee.get_cost())
