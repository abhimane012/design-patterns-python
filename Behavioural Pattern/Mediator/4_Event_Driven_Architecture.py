class EvenMediator:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, subscriber):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(subscriber)

    def unsubscribe(self, event_type, subscriber):
        if (
            event_type in self.subscribers
            and subscriber in self.subscribers[event_type]
        ):
            self.subscribers[event_type].remove(subscriber)

    def publish_event(self, event_type, data):
        for subscriber in self.subscribers[event_type]:
            subscriber.receive_event(event_type, data)
        print()


class Subscriber:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def subscribe(self, event_type):
        self.mediator.subscribe(event_type, self)

    def unsubscribe(self, event_type):
        self.mediator.unsubscribe(event_type, self)

    def receive_event(self, event_type, data):
        print(f"{self.name} receives data {data}")


if __name__ == "__main__":
    mediator = EvenMediator()

    sub1 = Subscriber("sub1", mediator)
    sub2 = Subscriber("sub2", mediator)
    sub3 = Subscriber("sub3", mediator)

    sub1.subscribe("Event1")
    sub1.subscribe("Event2")
    sub2.subscribe("Event1")
    sub2.subscribe("Event2")
    sub3.subscribe("Event1")

    mediator.publish_event("Event1", "Event1-data")
    mediator.publish_event("Event2", "Event2-data")
