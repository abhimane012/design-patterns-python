from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def request_handler(self, request):
        pass


class ConcreteHandler1(Handler):
    def request_handler(self, request):
        if request == "A":
            print(f"Request {request} is handled by handler 1")
        elif self.successor:
            print(f"Request {request} is not handled by handler 1")
            self.successor.request_handler(request)


class ConcreteHandler2(Handler):
    def request_handler(self, request):
        if request == "B":
            print(f"Request {request} is handled by handler 2")
        elif self.successor:
            print(f"Request {request} is not handled by handler 2")
            self.successor.request_handler(request)


class ConcreteHandler3(Handler):
    def request_handler(self, request):
        if request == "C":
            print(f"Request {request} is handled by handler 3")
        elif self.successor:
            print(f"Request {request} is not handled by handler 3")
            self.successor.request_handler(request)
        else:
            print(f"Request {request} is not handled by handler 3")
            print(f"Request handling is terminated")


if __name__ == "__main__":
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler3 = ConcreteHandler3()

    handler1.successor = handler2
    handler2.successor = handler3

    handler1.request_handler("C")
