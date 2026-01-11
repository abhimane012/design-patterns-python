from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit(self, element):
        pass


class ConcerteVisitor1(Visitor):
    def visit(self, element):
        element.operation1()
        print("more stuff going on with visitor 1")


class ConcerteVisitor2(Visitor):
    def visit(self, element):
        element.operation2()
        print("more stuff going on with visitor 2")


class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConcerteElementA(Element):
    def accept(self, visitor):
        visitor.visit(self)

    def operation1(self):
        print(f"{self.__class__.__name__} is performing {self.operation1.__name__}")

    def operation2(self):
        print(f"{self.__class__.__name__} is performing {self.operation2.__name__}")


class ConcerteElementB(Element):
    def accept(self, visitor):
        visitor.visit(self)

    def operation1(self):
        print(f"{self.__class__.__name__} is performing {self.operation1.__name__}")

    def operation2(self):
        print(f"{self.__class__.__name__} is performing {self.operation2.__name__}")


if __name__ == "__main__":
    element_a = ConcerteElementA()
    element_b = ConcerteElementB()

    visitor_1 = ConcerteVisitor1()
    visitor_2 = ConcerteVisitor2()

    element_a.accept(visitor_1)
    element_a.accept(visitor_2)

    element_b.accept(visitor_1)
    element_b.accept(visitor_2)
