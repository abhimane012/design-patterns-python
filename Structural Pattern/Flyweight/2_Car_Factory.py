# Car Factory
import random


class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.ship_to = None

    def info(self):
        print(f"Brand = {self.brand} Model = {self.model} ")
        print(f"Color = {self.color} Shipping to = {self.ship_to} ")
        print("-" * 30)


class CarFactory:
    _cars = {}
    _created = 0

    @staticmethod
    def create_car(brand, model, color):
        if (brand, model, color) in CarFactory._cars:
            return CarFactory._cars[(brand, model, color)]
        else:
            CarFactory._created += 1
            CarFactory._cars[(brand, model, color)] = Car(brand, model, color)
            return CarFactory._cars[(brand, model, color)]


if __name__ == "__main__":
    countrys = ["India", "China", "Nepal", "Russia", "USA", "UK", "Germany"]
    cars = [
        CarFactory.create_car("Toyota", "Innova", "Blue"),
        CarFactory.create_car("Toyota", "Innova", "Black"),
        CarFactory.create_car("Nissan", "GTR", "Silver"),
        CarFactory.create_car("Toyota", "Innova", "Blue"),
        CarFactory.create_car("Toyota", "Innova", "Blue"),
        CarFactory.create_car("Toyota", "Innova", "Black"),
        CarFactory.create_car("BMW", "M5", "Red"),
    ]

    for index, car in enumerate(cars, 1):
        print("Car : ", index)
        car.ship_to = random.choice(countrys)
        car.info()

    print()
    print(f"Created Cars = {CarFactory._created} and Total Shipped Cars = {len(cars)}")
