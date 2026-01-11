# Structural Pattern
class Service:
    def request(self):
        print(f"Provide Request from Service Provider")


class Adaptee:
    def complex_request(self):
        print(f"Provide complex request from Service Provider")


class Target:
    def request(self):
        pass


class Adapter(Target, Adaptee):
    def request(self):
        self.complex_request()


if __name__ == "__main__":
    service = Service()
    service.request()

    adapter = Adapter()
    adapter.request()
