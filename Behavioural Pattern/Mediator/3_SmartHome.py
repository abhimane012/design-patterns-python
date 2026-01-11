class SmartHomeMediator:
    def __init__(self):
        self.components = {}

    def register_component(self, component_name, component):
        self.components[component_name] = component

    def send_command(self, component_name, command):
        if component_name in self.components:
            self.components[component_name].execute_command(command)
        else:
            print(f"{component_name} doesn't exist")

    def get_component_state(self, component_name):
        if component_name in self.components:
            self.components[component_name].get_state()
        else:
            print(f"Component '{component_name}' not found.")


class SmartComponent:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        self.state = "OFF"

    def execute_command(self, command):
        pass

    def get_state(self):
        print(f"Current state of {self.name} {self.__class__.__name__} is {self.state}")


class AC(SmartComponent):
    def execute_command(self, command):
        if command == "ON":
            self.state = "ON"
            print(f"{self.name} AC turned ON.")
        elif command == "OFF":
            self.state = "OFF"
            print(f"{self.name} AC turned OFF.")
        elif command.startswith("SET_TEMP"):
            temperature = command.split(":")[1]  # startswith("SET_TEMP:22")
            self.state = f"ON (Temperature: {temperature})"
            print(f"{self.name} AC set to {temperature}°C.")


class Light(SmartComponent):
    def execute_command(self, command):
        if command == "ON":
            self.state = "ON"
            print(f"{self.name} Light turned ON.")
        elif command == "OFF":
            self.state = "OFF"
            print(f"{self.name} Light turned OFF.")


class TV(SmartComponent):
    def execute_command(self, command):
        if command == "ON":
            self.state = "ON"
            print(f"{self.name} TV turned ON.")
        elif command == "OFF":
            self.state = "OFF"
            print(f"{self.name} TV turned OFF.")


if __name__ == "__main__":
    smart_home_mediator = SmartHomeMediator()

    ac_1 = AC("Living Room", smart_home_mediator)
    ac_2 = AC("Bed Room", smart_home_mediator)

    light_1 = Light("Living Room", smart_home_mediator)
    light_2 = Light("Bed Room", smart_home_mediator)

    tv_1 = TV("Living Room", smart_home_mediator)
    tv_2 = TV("Bed Room", smart_home_mediator)

    smart_home_mediator.register_component("ac-1", ac_1)
    smart_home_mediator.register_component("ac-2", ac_2)

    smart_home_mediator.register_component("light-1", light_1)
    smart_home_mediator.register_component("light-2", light_2)

    smart_home_mediator.register_component("tv-1", tv_1)
    smart_home_mediator.register_component("tv-2", tv_2)

    smart_home_mediator.send_command("ac-1", "ON")
    smart_home_mediator.send_command("ac-1", "SET_TEMP:24")
    print()
    smart_home_mediator.send_command("light-1", "ON")
    smart_home_mediator.send_command("light-2", "ON")
    smart_home_mediator.send_command("light-1", "OFF")
    print()
    smart_home_mediator.send_command("tv-1", "ON")
    smart_home_mediator.send_command("tv-2", "ON")
    smart_home_mediator.send_command("tv-2", "OFF")
    print()

    smart_home_mediator.get_component_state("ac-1")
    smart_home_mediator.get_component_state("ac-2")
    smart_home_mediator.get_component_state("light-1")
    smart_home_mediator.get_component_state("light-2")
    smart_home_mediator.get_component_state("tv-1")
    smart_home_mediator.get_component_state("tv-2")
