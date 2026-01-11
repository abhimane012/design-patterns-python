# Example of builder pattern using director


class House:
    def __init__(self):
        self.wall = None
        self.roof = None
        self.floor = None
        self.furniture = dict()

    def __str__(self):
        return f"House(wall={self.wall},roof={self.roof},floor={self.floor},furniture={self.furniture})"


class HouseBuilder:
    def __init__(self):
        self.house = House()

    def set_wall(self, wall):
        self.house.wall = wall
        return self

    def set_roof(self, roof):
        self.house.roof = roof
        return self

    def set_floor(self, floor):
        self.house.floor = floor
        return self

    def set_furniture(self, name, amount):
        if self.house.furniture.get(name, None):
            self.house.furniture[name] += amount
        else:
            self.house.furniture[name] = amount
        return self

    def get_house(self):
        return self.house


class SmallHouseBuilder(HouseBuilder):

    def build_wall(self):
        self.set_wall(10)

    def build_roof(self):
        self.set_roof(10)

    def build_floor(self):
        self.set_floor(10)

    def build_furniture(self):
        self.set_furniture("chairs", 10)
        self.set_furniture("fan", 10)
        self.set_furniture("sofa", 10)


class BigHouseBuilder(HouseBuilder):

    def build_wall(self):
        self.set_wall(50)

    def build_roof(self):
        self.set_roof(50)

    def build_floor(self):
        self.set_floor(50)

    def build_furniture(self):
        self.set_furniture("chairs", 30)
        self.set_furniture("fan", 30)
        self.set_furniture("sofa", 30)


class Contractor:  # Director
    def __init__(self, builder):
        self.builder = builder

    def build_house(self):
        self.builder.build_wall()
        self.builder.build_roof()
        self.builder.build_floor()
        self.builder.build_furniture()


if __name__ == "__main__":
    small_house_builder = SmallHouseBuilder()
    big_house_builder = BigHouseBuilder()

    contractor = Contractor(small_house_builder)
    contractor.build_house()
    small_house = small_house_builder.get_house()
    print(small_house)

    contractor = Contractor(big_house_builder)
    contractor.build_house()
    big_house = big_house_builder.get_house()
    print(big_house)
