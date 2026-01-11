# Example of simple builder pattern


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


print("====Small Hosue Builder====")
small_house_builder = HouseBuilder()
small_house_builder.set_wall(10).set_roof(10).set_floor(10).set_furniture(
    "chairs", 10
).set_furniture("chairs", 10).set_furniture("fans", 10)
small_house = small_house_builder.get_house()
print(small_house)

print("====Big Hosue Builder====")
big_house_builder = HouseBuilder()
big_house_builder.set_wall(10).set_roof(10).set_floor(10).set_furniture(
    "chairs", 10
).set_furniture("chairs", 10).set_furniture("fans", 25)
big_house = big_house_builder.get_house()
print(big_house)
