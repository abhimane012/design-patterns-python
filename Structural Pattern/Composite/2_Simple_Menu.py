# Simple Menu Using Composite


class Menu:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"--- {self.name}")


class MenuComponent:
    def __init__(self, name):
        self.menu_name = name
        self.menus = []

    def add(self, menu):
        self.menus.append(menu)

    def remove(self, menu):
        self.menus.remove(menu)

    def display(self):
        print(f"{self.menu_name}".center(30, "-"))
        for submenu in self.menus:
            submenu.display()


if __name__ == "__main__":
    menu1 = MenuComponent("Breakfast")
    menu2 = MenuComponent("Snacks")
    menu3 = MenuComponent("Cold-Drinks")

    menu1.add(Menu("Idli"))
    menu1.add(Menu("Dosa"))
    menu1.add(Menu("Benne Dosa"))
    menu1.add(Menu("Masala Dosa"))

    menu2.add(Menu("Samosa"))
    menu2.add(Menu("Chat"))
    menu2.add(Menu("Panipuri"))
    menu2.add(Menu("Kachori"))

    menu3.add(Menu("Coke"))
    menu3.add(Menu("Limca"))
    menu3.add(Menu("Sprite"))
    menu3.add(Menu("Thubms-Up"))

    menu1.add(menu2)
    menu1.add(menu3)

    menu1.display()
