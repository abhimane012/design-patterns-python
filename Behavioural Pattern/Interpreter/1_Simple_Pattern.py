# Simple Interpreter Design Pattern Example

from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def interprete(self):
        pass


class Number(Expression):
    def __init__(self, no):
        self.value = no

    def interprete(self):
        return self.value


class Addition(Expression):
    def __init__(self, exp1, exp2):
        self.expression1 = exp1
        self.expression2 = exp2

    def interprete(self):
        return self.expression1.interprete() + self.expression2.interprete()


class Subtraction(Expression):
    def __init__(self, exp1, exp2):
        self.expression1 = exp1
        self.expression2 = exp2

    def interprete(self):
        return self.expression1.interprete() - self.expression2.interprete()


class Multiplication(Expression):
    def __init__(self, exp1, exp2):
        self.expression1 = exp1
        self.expression2 = exp2

    def interprete(self):
        return self.expression1.interprete() * self.expression2.interprete()


class Division(Expression):
    def __init__(self, exp1, exp2):
        self.expression1 = exp1
        self.expression2 = exp2

    def interprete(self):
        return self.expression1.interprete() / self.expression2.interprete()


if __name__ == "__main__":
    num1 = Number(12)
    num2 = Number(8)
    num3 = Number(5)
    num4 = Number(3)

    exp = Addition(Addition(num1, Subtraction(num2, num3)), Multiplication(num3, num4))
    print(exp.interprete())
