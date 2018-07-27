class Greeter:
    def greet(self):
        pass


class RealGreeter(Greeter):
    def greet(self):
        return ("Hi there")


class ProxyGreeter(Greeter):
    def __init__(self):
        self.greeter = None

    def greet(self):
        # 1 Lookup greeter object on network and send request to call greet() method
        # 2 Check if the user is authorized to access
        # 3 Cache content
        if self.greeter is None:
            self.greeter = RealGreeter()
        return self.greeter.greet()


greeter = ProxyGreeter()
print(greeter.greet())
print(greeter.greet())
