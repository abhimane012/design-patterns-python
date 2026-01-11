# House building factory example

from abc import ABC, abstractmethod


#########PROUCCT-1############
class Furniture(ABC):
    def __init__(self, quantity):
        self.quantity = quantity

    @abstractmethod
    def display(self):
        pass


class Sofa(Furniture):
    def display(self):
        print(f"{self.quantity} sofas")


class Table(Furniture):
    def display(self):
        print(f"{self.quantity} table")


class Bed(Furniture):
    def display(self):
        print(f"{self.quantity} beds")


#########PROUCCT-2############
class Electronics(ABC):
    def __init__(self, quantity):
        self.quantity = quantity

    @abstractmethod
    def display(self):
        pass


class TV(Electronics):
    def display(self):
        print(f"{self.quantity} TVs")


class Monitor(Electronics):
    def display(self):
        print(f"{self.quantity} Monitor")


#########PROUCCT-3############
class Decorations(ABC):
    def __init__(self, quantity):
        self.quantity = quantity

    @abstractmethod
    def display(self):
        pass


class FlowerVase(Decorations):
    def display(self):
        print(f"{self.quantity} flowervases")


class Idols(Decorations):
    def display(self):
        print(f"{self.quantity} Idols")


############HouseFactory##########


class HouseFactory(ABC):
    @abstractmethod
    def furniture(self):
        pass

    @abstractmethod
    def electronics(self):
        pass

    @abstractmethod
    def decorations(self):
        pass


class SmallHouse(HouseFactory):
    def furniture(self):
        return Sofa(10)

    def electronics(self):
        return TV(20)

    def decorations(self):
        return FlowerVase(20)


class BigHouse(HouseFactory):
    def furniture(self):
        return Table(20)

    def electronics(self):
        return Monitor(30)

    def decorations(self):
        return Idols(40)


##### client code #####
def client(factory: HouseFactory):
    factory.furniture().display()
    factory.electronics().display()
    factory.decorations().display()
    print()


if __name__ == "__main__":
    print("SMALL_HOUSE".center(30, "*"))
    client(SmallHouse())

    print("BIG_HOUSE".center(30, "*"))
    client(BigHouse())
