# Update Company stock price to different stock market!


class Observable:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, update, msg):  # update_observers
        for observer in self.observers:
            observer.update(update, msg)


class Observer:
    def update(self, *args, **kwargs):
        pass


class AmericanStockMarket(Observer):
    def update(self, update, msg):
        print ("American stock market received: {0} {1}".format(update, msg))


class EuropeanStockMarket(Observer):
    def update(self, update, msg):
        print ("European stock market received: {0} {1}".format(update, msg))


company = Observable()

american_observer = AmericanStockMarket()
european_observer = EuropeanStockMarket()

company.register(american_observer)
company.register(european_observer)

company.notify_observers('important update:', msg='CEO quits')
