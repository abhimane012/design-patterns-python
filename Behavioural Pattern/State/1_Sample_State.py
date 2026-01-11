from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def do_action(self, context):
        pass


class StateA(State):
    def do_action(self, context):
        print(f"{self.__class__.__name__} is performing some Action.........")
        context.state = StateB()


class StateB(State):
    def do_action(self, context):
        print(f"{self.__class__.__name__} is performing some Action.........")
        context.state = StateC()


class StateC(State):
    def do_action(self, context):
        print(f"{self.__class__.__name__} is performing some Action.........")
        context.state = StateD()


class StateD(State):
    def do_action(self, context):
        print(f"{self.__class__.__name__} is performing some Action.........")
        context.state = StateA()


class Context:
    def __init__(self):
        self.state = StateA()

    def request(self):
        self.state.do_action(self)


if __name__ == "__main__":
    context = Context()
    context.request()
    context.request()
    context.request()
    context.request()
    context.request()
