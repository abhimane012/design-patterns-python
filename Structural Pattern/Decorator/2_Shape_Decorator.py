# Shape Decorator
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle...")


class ShapeDecorator(Shape):
    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        self.shape.draw()


class RedShapeDecorator(ShapeDecorator):
    def draw(self):
        self.shape.draw()
        self.red_color()

    def red_color(self):
        print(f"Painting {self.shape.__class__.__name__} in Red Color...")


class BlueShapeDecorator(ShapeDecorator):
    def draw(self):
        self.shape.draw()
        self.blue_color()

    def blue_color(self):
        print(f"Painting {self.shape.__class__.__name__} in Blue Color...")


class OrangeShapeDecorator(ShapeDecorator):
    def draw(self):
        self.shape.draw()
        self.orange_color()

    def orange_color(self):
        print(f"Painting {self.shape.__class__.__name__} in Orange Color...")


if __name__ == "__main__":
    rect = Rectangle()
    rect.draw()

    red_shape_decorator = RedShapeDecorator(rect)
    red_shape_decorator.draw()

    blue_shape_decorator = BlueShapeDecorator(rect)
    blue_shape_decorator.draw()

    orange_shape_decorator = OrangeShapeDecorator(rect)
    orange_shape_decorator.draw()
