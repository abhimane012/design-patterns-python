from abc import ABC, abstractmethod


class TV:
    def turn_on_tv(self):
        print("Turnning on TV!")

    def turn_off_tv(self):
        print("Turning of TV!")


class Command(ABC):
    def __init__(self, tv):
        self.tv = tv

    @abstractmethod
    def execute(self):
        pass


class TurnOnTvCommand(Command):
    def execute(self):
        self.tv.turn_on_tv()


class TurnOffTvCommand(Command):
    def execute(self):
        self.tv.turn_off_tv()


class RemoteControl:
    def __init__(self, command=None):
        self.command = command

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        self.command.execute()


if __name__ == "__main__":
    tv = TV()

    turn_on_command = TurnOnTvCommand(tv)
    turn_off_command = TurnOffTvCommand(tv)

    remote = RemoteControl()
    remote.set_command(turn_on_command)
    remote.execute_command()

    remote.set_command(turn_off_command)
    remote.execute_command()
