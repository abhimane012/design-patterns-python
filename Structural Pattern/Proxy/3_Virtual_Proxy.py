# Virtual Proxy Lazy Loading

from abc import ABC, abstractmethod


class Image(ABC):
    @abstractmethod
    def display(self):
        pass


class RealImage(Image):
    def __init__(self, file_name):
        self.file_name = file_name
        self.load_from_disk()

    def display(self):
        print(f"Displaying {self.file_name} .......")

    def load_from_disk(self):
        print(f"Loading {self.file_name} from disk....")


class ProxyImage(Image):
    def __init__(self, file_name):
        self.file_name = file_name
        self.real_image = None

    def display(self):
        if not self.real_image:
            self.real_image = RealImage(self.file_name)
        self.real_image.display()


if __name__ == "__main__":
    proxy_image_1 = ProxyImage("Image1.png")
    proxy_image_2 = ProxyImage("Image2.png")
    proxy_image_3 = ProxyImage("Image3.png")

    proxy_image_1.display()
    proxy_image_2.display()
    proxy_image_3.display()
    proxy_image_1.display()
    proxy_image_2.display()
    proxy_image_3.display()
