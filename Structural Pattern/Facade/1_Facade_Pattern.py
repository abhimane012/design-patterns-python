# Facade Pattern


class SubSystem1:
    def operation1(self):
        print("Subsystem1 Performing operation1")

    def operation2(self):
        print("Subsystem1 Performing operation2")


class SubSystem2:
    def operation1(self):
        print("Subsystem2 Performing operation1")

    def operation2(self):
        print("Subsystem2 Performing operation2")


class Facade:
    def __init__(self):
        self.subsystem1 = SubSystem1()
        self.subsystem2 = SubSystem2()

    def operation1(self):
        self.subsystem1.operation1()
        self.subsystem2.operation1()

    def operation2(self):
        self.subsystem1.operation2()
        self.subsystem2.operation2()


if __name__ == "__main__":
    facade = Facade()

    facade.operation1()
    facade.operation2()
