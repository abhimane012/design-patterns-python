from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class HelloCommand1(Command):
    def execute(self):
        print(f"Hello, Command - 1!!")


class HelloCommand2(Command):
    def execute(self):
        print(f"Hello, Command - 2!!")


class HelloCommand3(Command):
    def execute(self):
        print(f"Hello, Command - 3!!")


class Invoker:
    def __init__(self):
        self.commands = []

    def set_command(self, command):
        self.commands.append(command)

    def execute_command(self):
        for command in self.commands:
            command.execute()


if __name__ == "__main__":
    cmd1 = HelloCommand1()
    cmd2 = HelloCommand2()
    cmd3 = HelloCommand3()

    invoker = Invoker()

    invoker.set_command(cmd1)
    invoker.set_command(cmd2)
    invoker.set_command(cmd3)

    invoker.execute_command()
