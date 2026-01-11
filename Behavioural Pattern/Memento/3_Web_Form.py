class FormMemento:
    def __init__(self, data):
        self.form_data = data

    def get_form_data(self):
        return self.form_data


class CareTaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, data):
        self.mementos.append(data)

    def goto_page(self, index):
        return self.mementos[index]


class Form:
    def __init__(self):
        self.data = {}

    def set_field(self, field_name, value):
        self.data[field_name] = value

    def get_field(self, field_name):
        return self.data[field_name]

    def save_form(self):
        return FormMemento(dict(self.data))

    def restore_form_data(self, memento):
        self.data = memento.get_form_data()

    def print_form(self):
        for field, value in self.data.items():
            print(f"{field} : {value}")
        print("*" * 30)


if __name__ == "__main__":
    form = Form()
    care_taker = CareTaker()

    form.set_field("name", "Abhishek")
    form.set_field("last name", "Mane")
    form.set_field("gender", "Male")
    care_taker.add_memento(form.save_form())
    form.print_form()

    form.set_field("Age", "24")
    form.set_field("Blood Group", "AB+ve")
    form.set_field("Height", "5ft 6inch")
    care_taker.add_memento(form.save_form())
    form.print_form()

    form.set_field("Device", "Macbook")
    form.set_field("Profession", "Software Engineer")
    form.set_field("City", "Banglore")
    care_taker.add_memento(form.save_form())
    form.print_form()

    form.restore_form_data(care_taker.goto_page(0))
    form.print_form()
