# Cache Proxys

from abc import ABC, abstractmethod
import random


class Request(ABC):
    @abstractmethod
    def request(self, key):
        pass


class RemoteServer(Request):
    def __init__(self):
        self.cache = {}

    def request(self, key):
        self.cache[key] = random.randint(1, 1000)
        print(f"RemoteServer: Processing request for key '{key}'")
        print(f"Data for '{key}' is {self.cache[key]}")


class ProxyServer(Request):
    def __init__(self, remote_server):
        self.remote_server = remote_server

    def request(self, key):
        if key in self.remote_server.cache:
            print(f"Proxy Server: Serving data for key {key} from cache")
            print(f"Cached data for {key} is {self.remote_server.cache[key]}")
        else:
            self.remote_server.request(key)
            print(f"Proxy Server: Caching data for key {key}")


if __name__ == "__main__":
    remote_server = RemoteServer()
    proxy_server = ProxyServer(remote_server)
    proxy_server.request("Key1")
    proxy_server.request("Key2")
    proxy_server.request("Key3")
    proxy_server.request("Key1")
    proxy_server.request("Key3")
    proxy_server.request("Key2")
