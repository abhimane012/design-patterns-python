# Simple factory method pattern

from abc import ABC, abstractmethod


class Product(ABC):  # E.g - Vehicle
    @abstractmethod
    def operation(self):
        pass


class ConcreteProductA(Product):  # E.g - Car
    def operation(self):
        return "ConcreteProductA Operation is performed"


class ConcreteProductB(Product):  # E.g - Bike
    def operation(self):
        return "ConcreteProductB Operation is performed"


class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass


class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()


if __name__ == "__main__":
    creator_a = ConcreteCreatorA()
    product_a = creator_a.factory_method()
    print(product_a.operation())

    creator_b = ConcreteCreatorB()
    product_b = creator_b.factory_method()
    print(product_b.operation())
