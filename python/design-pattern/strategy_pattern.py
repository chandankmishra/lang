from abc import ABC, abstractmethod


class File:
    def __init__(self):
        self.strategy = None

    def compress(self):
        self.strategy.compress()


class StategyPattern(ABC):
    @abstractmethod
    def compress(self):
        raise ImplementationError


class ZipStrategy(StategyPattern):
    def compress(self):
        print ("Compress with ZIP")


class RarStrategy(StategyPattern):
    def __init__(self):
        pass

    def compress(self):
        print ("Compress with RAR")


f = File()
f.strategy = ZipStrategy()
f.compress()
f.strategy = RarStrategy()
f.compress()
