from abc import ABC, abstractmethod


class StockMarket:
    def __init__(self):
        self.observers = []
        self.stocks = {}

    def subscribe(self, investor):
        self.observers.append(investor)

    def unsubscribe(self, investor):
        self.observers.remove(investor)

    def add_update_stock(self, symbol, price):
        self.stocks[symbol] = price
        self.notify(symbol)

    def notify(self, symbol):
        for observer in self.observers:
            observer.update(symbol, self.stocks[symbol])
        print()


class Observer(ABC):
    @abstractmethod
    def update(self, symbol, price):
        pass


class Investor(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, symbol, price):
        print(f"Investor {self.name}: Stock {symbol} price is now: ₹{price}")


if __name__ == "__main__":
    stock_market = StockMarket()
    investor1 = Investor("Abhishek")
    investor2 = Investor("Hrishi")

    stock_market.subscribe(investor1)
    stock_market.subscribe(investor2)

    stock_market.add_update_stock("Apple", 100)
    stock_market.add_update_stock("TCS", 10)
    stock_market.add_update_stock("HDFC", 90)
    stock_market.add_update_stock("RELIANCE", 40)

    stock_market.add_update_stock("Apple", 140)
    stock_market.add_update_stock("TCS", 40)
    stock_market.unsubscribe(investor2)
    stock_market.add_update_stock("HDFC", 95)
    stock_market.add_update_stock("RELIANCE", 120)
