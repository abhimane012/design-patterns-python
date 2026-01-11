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

    def __iter__(self):
        return self


if __name__ == "__main__":
    list_data = [
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
    ]

    my_iterator = MyIterator(list_data)

    for item in my_iterator:
        print(item)
