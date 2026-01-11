from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass


class BubbleSortStrategy(Strategy):
    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]


class QuickSortStrategy(Strategy):
    def sort(self, data):
        self._quick_sort(data, 0, len(data) - 1)

    def _quick_sort(self, data, low, high):
        if low < high:
            pivot_index = self._partition(data, low, high)
            self._quick_sort(data, low, pivot_index - 1)
            self._quick_sort(data, pivot_index + 1, high)

    def _partition(self, data, low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1


class Sorter:
    def __init__(self, sort_strategy):
        self.sorting_strategy = sort_strategy

    def set_sorting_strategy(self, sort_strategy):
        self.sorting_strategy = sort_strategy

    def sort_data(self, data):
        self.sorting_strategy.sort(data)


if __name__ == "__main__":
    bubble_sorter = BubbleSortStrategy()
    quick_sorter = QuickSortStrategy()

    sorter = Sorter(bubble_sorter)

    data = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    sorter.sort_data(data)

    print(data)

    sorter.set_sorting_strategy(quick_sorter)

    data = [
        "Alex",
        "Benjamin",
        "Charlotte",
        "Daniel",
        "Emma",
        "Grace",
        "Henry",
        "Isabella",
        "James",
        "Liam",
        "Mia",
        "Noah",
        "Olivia",
        "Sophia",
        "William",
    ]

    sorter.sort_data(data)

    print(data)
