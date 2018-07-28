from abc import ABC, abstractmethod


class CompressClient:
    def __init__(self):
        self.strategy = None

    def compress(self):
        self.strategy.compress()

# Abstract Interface


class StategyPattern(ABC):
    @abstractmethod
    def compress(self):
        pass


class ZipStrategy(StategyPattern):
    def compress(self):
        print ("Compress with ZIP")


class RarStrategy(StategyPattern):
    def compress(self):
        print ("Compress with RAR")


f = CompressClient()
f.strategy = ZipStrategy()
f.compress()
f.strategy = RarStrategy()
f.compress()
