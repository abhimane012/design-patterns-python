# Composite Pattern
class Component:
    def __init__(self, name):
        self.name = name

    def operation(self):
        print(f"{self.name}: Performing Operation")


class Composite:
    def __init__(self):
        self.components = []

    def add(self, component):
        self.components.append(component)

    def remove(self, component):
        self.components.remove(component)

    def operation(self):
        for child in self.components:
            child.operation()


if __name__ == "__main__":
    components = Composite()
    leaf1 = Component("Leaf-1")
    leaf2 = Component("Leaf-2")
    leaf3 = Component("Leaf-3")
    leaf4 = Component("Leaf-4")
    components.add(leaf1)
    components.add(leaf2)
    components.add(leaf3)
    components.add(leaf4)
    components.operation()

    print()

    components = Composite()
    leaf5 = Component("Leaf-5")
    leaf6 = Component("Leaf-6")
    leaf7 = Component("Leaf-7")
    leaf8 = Component("Leaf-8")
    components.add(leaf5)
    components.add(leaf6)
    components.add(leaf7)
    components.add(leaf8)
    components.operation()
