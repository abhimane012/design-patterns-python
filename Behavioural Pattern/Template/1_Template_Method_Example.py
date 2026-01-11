from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self):
        self.initialize()
        self.perform_algorithm()
        self.cleanup()

    def initialize(self):
        print(f"Initializing Algorithm for {self.__class__.__name__}")

    @abstractmethod
    def perform_algorithm(self):
        pass

    def cleanup(self):
        print(f"Performing Cleanup for {self.__class__.__name__}")


class ConcreteClass1(AbstractClass):
    def perform_algorithm(self):
        print(f"Performing Alogrithm for {self.__class__.__name__}")


class ConcreteClass2(AbstractClass):
    def perform_algorithm(self):
        print(f"Performing Alogrithm for {self.__class__.__name__}")


if __name__ == "__main__":
    class1 = ConcreteClass1()
    class1.template_method()

    print()

    class2 = ConcreteClass2()
    class2.template_method()
