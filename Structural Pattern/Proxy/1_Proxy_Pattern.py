# Proxy Pattern
from abc import ABC, abstractmethod


class SubjectInterface(ABC):
    @abstractmethod
    def perform_operation(self):
        pass


class RealSubject(SubjectInterface):
    def perform_operation(self):
        print("Performing action on real subject")


class ProxySubject(SubjectInterface):
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def perform_operation(self):
        print("Proxy: Performing Some operation")
        self.real_subject.perform_operation()


if __name__ == "__main__":
    real_subject = RealSubject()
    proxy_subject = ProxySubject(real_subject)
    proxy_subject.perform_operation()
