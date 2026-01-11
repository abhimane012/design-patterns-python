class MyIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def has_next(self):
        return self.index < len(self.iterable)

    def __next__(self):
        if self.has_next():
            item = self.iterable[self.index]
            self.index += 1
            return item
        else:
            self.index = 0
            raise StopIteration


class MyCollection:
    def __init__(self):
        self.data = []

    def insert_data(self, item):
        self.data.append(item)

    def __iter__(self):
        return MyIterator(self.data)


if __name__ == "__main__":
    collection = MyCollection()
    collection.insert_data("Item-1")
    collection.insert_data("Item-2")
    collection.insert_data("Item-3")
    collection.insert_data("Item-4")
    collection.insert_data("Item-5")
    collection.insert_data("Item-6")

    for item in collection:
        print(item)
