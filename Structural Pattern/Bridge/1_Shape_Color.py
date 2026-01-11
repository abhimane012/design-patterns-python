# Shape and Color Bridge pattern exampl

from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        pass


class Circle(Shape):
    def __str__(self):
        return f"This is {self.color.name()} Circle"


class Square(Shape):
    def __str__(self):
        return f"This is {self.color.name()} Square"


class Rectangle(Shape):
    def __str__(self):
        return f"This is {self.color.name()} Rectangle"


class Color(ABC):
    def name(self):
        pass


class Red(Color):
    def name(self):
        return "Red"


class Green(Color):
    def name(self):
        return "Green"


class Blue(Color):
    def name(self):
        return "Blue"


if __name__ == "__main__":
    red = Red()
    green = Green()
    blue = Blue()

    circle = Circle(red)
    print(circle)

    rect = Rectangle(green)
    print(rect)

    sqrt = Square(blue)
    print(sqrt)
