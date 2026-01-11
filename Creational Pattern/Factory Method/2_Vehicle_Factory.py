# Vehicle factory example
# This is example of factory pattern rest all are example of factory method

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print(f"Car is starting......")


class Bike(Vehicle):
    def start(self):
        print(f"Bike is starting......")


class Truck(Vehicle):
    def start(self):
        print(f"Truck is starting......")


class Motorcycle(Vehicle):
    def start(self):
        print(f"Motorcycle is starting......")


class VehicleFactory:
    def __init__(self):
        self.factory = dict(car=Car, bike=Bike, truck=Truck, motorcycle=Motorcycle)

    def create_vehicle(self, vehicle_type):
        if vehicle_type in self.factory:
            Vehicle = self.factory.get(vehicle_type)
            return Vehicle()


if __name__ == "__main__":
    vehicle_factory = VehicleFactory()

    car = vehicle_factory.create_vehicle("car")
    car.start()

    bike = vehicle_factory.create_vehicle("bike")
    bike.start()

    truck = vehicle_factory.create_vehicle("truck")
    truck.start()

    motorcycle = vehicle_factory.create_vehicle("motorcycle")
    motorcycle.start()
