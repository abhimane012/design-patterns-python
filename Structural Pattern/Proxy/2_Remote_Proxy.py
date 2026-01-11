# Remote Proxy Pattern
from abc import ABC, abstractmethod


class RemoteService(ABC):
    @abstractmethod
    def perform_operation(self):
        pass


class RemoteServiceImplementation(RemoteService):
    def perform_operation(self):
        print("Performing action at Remote Service")


class RemoteServiceProxy(RemoteService):
    def __init__(self, remote_service):
        self.remote_service = remote_service

    def perform_operation(self):
        print("Proxy: Performing Some operation before invoking remote service")
        self.remote_service.perform_operation()
        print("Proxy: Performing Some operation after invoking remote service")


if __name__ == "__main__":
    remote_service = RemoteServiceImplementation()
    proxy_service = RemoteServiceProxy(remote_service)
    proxy_service.perform_operation()
