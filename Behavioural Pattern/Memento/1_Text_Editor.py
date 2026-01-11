class Memento:
    def __init__(self, content):
        self.saved_content = content

    def get_saved_content(self):
        return self.saved_content


class CareTaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]


class Editor:
    def __init__(self):
        self.content = ""

    def add_text(self, text):
        self.content += text

    def create_memento(self):
        return Memento(self.content)

    def restore_memento(self, memento):
        self.content = memento.get_saved_content()

    def get_content(self):
        return self.content


if __name__ == "__main__":
    editor = Editor()
    care_taker = CareTaker()

    editor.add_text("Hi,")
    care_taker.add_memento(editor.create_memento())
    editor.add_text(" My name")
    care_taker.add_memento(editor.create_memento())
    editor.add_text(" is Abhishek ")
    care_taker.add_memento(editor.create_memento())
    editor.add_text("Vinayak Mane ")
    care_taker.add_memento(editor.create_memento())
    print(editor.get_content())

    editor.restore_memento(care_taker.get_memento(0))
    print(editor.get_content())

    editor.restore_memento(care_taker.get_memento(2))
    print(editor.get_content())

    editor.restore_memento(care_taker.get_memento(1))
    print(editor.get_content())
