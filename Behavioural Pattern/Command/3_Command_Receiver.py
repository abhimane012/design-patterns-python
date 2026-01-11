from abc import ABC, abstractmethod


class Greet:
    def english(self):
        print(f"Hello and welcome !")

    def spanish(self):
        print(f"Hola y bienvenido !")

    def french(self):
        print(f"Bonjour et bienvenue !")

    def german(self):
        print(f"Hallo und willkommen !")

    def italian(self):
        print(f"Ciao e benvenuto !")

    def japanese(self):
        print(f"こんにちは ようこそ です !")

    def chinese(self):
        print(f"你好 欢迎 你 !")

    def arabic(self):
        print(f"مرحبا و أهل !")


class Command(ABC):
    def __init__(self, greet):
        self._greet = greet

    @abstractmethod
    def execute(self):
        pass


class Hello_English(Command):
    def execute(self):
        self._greet.english()


class Hello_French(Command):
    def execute(self):
        self._greet.french()


class Hello_Italian(Command):
    def execute(self):
        self._greet.italian()


class Hello_Chinese(Command):
    def execute(self):
        self._greet.chinese()


class Hello_Arabic(Command):
    def execute(self):
        self._greet.arabic()


class Invoker:
    def __init__(self, commands=[]):
        self.commands = commands

    def set_command(self, command):
        self.commands.append(command)

    def execute_command(self):
        for command in self.commands:
            command.execute()


if __name__ == "__main__":
    greets = Greet()
    english = Hello_English(greets)
    french = Hello_French(greets)
    italian = Hello_Italian(greets)
    chinese = Hello_Chinese(greets)
    arabic = Hello_Arabic(greets)

    invoker = Invoker()
    invoker.set_command(english)
    invoker.set_command(french)
    invoker.set_command(italian)
    invoker.set_command(chinese)
    invoker.set_command(arabic)

    invoker.execute_command()
