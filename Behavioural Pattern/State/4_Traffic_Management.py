from abc import ABC, abstractmethod


class TrafficLight(ABC):
    @abstractmethod
    def display_light(self):
        pass

    @abstractmethod
    def change_light(self, traffic_light):
        pass


class RedLight(TrafficLight):
    def display_light(self):
        return "RED"

    def change_light(self, traffic_light):
        print(f"Changing Light from RED to GREEN")
        traffic_light.state = GreenLight()


class GreenLight(TrafficLight):
    def display_light(self):
        return "GREEN"

    def change_light(self, traffic_light):
        print(f"Changing Light from GREEN to YELLOW")
        traffic_light.state = YellowLight()


class YellowLight(TrafficLight):
    def display_light(self):
        return "YELLOW"

    def change_light(self, traffic_light):
        print(f"Changing Light from YELLOW to RED")
        traffic_light.state = RedLight()


class TrafficLightSignal:
    def __init__(self):
        self.state = RedLight()

    def display_light(self):
        print(self.state.display_light())

    def change_light(self):
        self.state.change_light(self)


if __name__ == "__main__":
    traffic_light = TrafficLightSignal()

    traffic_light.display_light()
    traffic_light.change_light()
    print()

    traffic_light.display_light()
    traffic_light.change_light()
    print()

    traffic_light.display_light()
    traffic_light.change_light()
    print()

    traffic_light.display_light()
    traffic_light.change_light()
    print()
