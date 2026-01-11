from abc import ABC, abstractmethod


class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observer.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)
        print()


class WeatherStation(Subject):
    def set_weather(self, message):
        print(f"Weather station setting weather to: {message}")
        self.notify(message)


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class MobileApp(Observer):
    def update(self, message):
        print(f"{self.__class__.__name__}: Received weather update -", message)


class DesktopApp(Observer):
    def update(self, message):
        print(f"{self.__class__.__name__}: Received weather update -", message)


if __name__ == "__main__":
    weather_station = WeatherStation()
    mobile_app = MobileApp()
    desktop_app = DesktopApp()

    weather_station.subscribe(mobile_app)
    weather_station.subscribe(desktop_app)

    weather_station.set_weather("Sunny")
    weather_station.set_weather("Rainy")
