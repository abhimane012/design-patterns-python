# Singleton class example


class Singleton:
    __instance = None

    def __init__(self, name: str):
        self.name = name
        if not Singleton.__instance:
            Exception("Object Already Exists")
        Singleton.__instance = self

    @staticmethod
    def get_instance(name: str):
        if not Singleton.__instance:
            Singleton(name)
        return Singleton.__instance


n1 = Singleton.get_instance("Abhishek")
n2 = Singleton.get_instance("Ramesh")

print(id(n1))
print(id(n2))
