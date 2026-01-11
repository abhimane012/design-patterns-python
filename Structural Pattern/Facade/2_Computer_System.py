# Computer System


class CPU:
    def freeze(self):
        print("CPU Freeze")

    def jump(self, position):
        print(f"jump to address {position}")

    def execute(self):
        print("executing data")


class Memory:
    def __init__(self):
        self.data = {}

    def load(self, data, position):
        print(f"Load data {data} @ address {position}")
        self.data[position] = data

    def get_data(self, position):
        print(f"get the data from {position}....")
        return self.data[position]


class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()

    def run(self, program):
        self.cpu.freeze()
        position = 0

        for instruction in program:
            self.memory.load(instruction, position)
            self.cpu.jump(position)
            self.cpu.execute()
            position += 1
            print()

    def retrieve(self, position):
        return self.memory.get_data(position)


if __name__ == "__main__":
    computer = Computer()
    program = [2342, 4553, 444, "Hello World", 25322]
    computer.run(program)
