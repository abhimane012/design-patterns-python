from abc import ABC, abstractmethod


class Handlder(ABC):
    def __init__(self):
        self.successor = None

    @abstractmethod
    def budget_request(self, request_amount):
        pass


class TeamLead(Handlder):
    def budget_request(self, request_amount):
        if request_amount <= 5000:
            print(f"The Requested amount {request_amount} is approved by TeamLead")
        elif self.successor:
            self.successor.budget_request(request_amount)


class Manager(Handlder):
    def budget_request(self, request_amount):
        if request_amount <= 10000:
            print(f"The Requested amount {request_amount} is approved by Manager")
        elif self.successor:
            self.successor.budget_request(request_amount)


class VicePresident(Handlder):
    def budget_request(self, request_amount):
        if request_amount <= 15000:
            print(f"The Requested amount {request_amount} is approved by VicePresident")
        elif self.successor:
            self.successor.budget_request(request_amount)


class President(Handlder):
    def budget_request(self, request_amount):
        if request_amount <= 25000:
            print(f"The Requested amount {request_amount} is approved by President")
        elif self.successor:
            self.successor.budget_request(request_amount)


class CEO(Handlder):
    def budget_request(self, request_amount):
        if request_amount <= 50000:
            print(f"The Requested amount {request_amount} is approved by CEO")
        elif self.successor:
            self.successor.budget_request(request_amount)
        else:
            print(f"The Requested amount {request_amount} is beyond the limits")


if __name__ == "__main__":
    team_lead = TeamLead()
    manager = Manager()
    vice_president = VicePresident()
    president = President()
    ceo = CEO()

    team_lead.successor = manager
    manager.successor = vice_president
    vice_president.successor = president
    president.successor = ceo

    team_lead.budget_request(51000)
