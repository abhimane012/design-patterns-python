# Prototype Pattern
import copy


class Square:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Prototype:
    def __init__(self):
        self.obj = dict()

    def register_object(self, name, obj):
        self.obj[name] = obj

    def deregister_object(self, name):
        del self.obj[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self.obj[name])
        obj.__dict__.clear()
        obj.__dict__.update(attr)
        return obj


if __name__ == "__main__":
    sq = Square(10, 20)
    proto = Prototype()
    proto.register_object("square", sq)

    rect = proto.clone("square", x=40, y=80)
    cube = proto.clone("square", l=10, b=20, h=30)
