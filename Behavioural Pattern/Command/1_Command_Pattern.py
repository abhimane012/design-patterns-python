from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class HelloCommand(Command):
    def execute(self):
        print(f"Hello, Command!!")


class Invoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        self.command.execute()


if __name__ == "__main__":
    hello = HelloCommand()
    invoker = Invoker()
    invoker.set_command(hello)
    invoker.execute_command()
