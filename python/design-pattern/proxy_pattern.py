class GreeterInterface:
    def greet(self):
        pass


class RealGreeter(GreeterInterface):
    def greet(self):
        return ("The real thing is dealing with the request")


class ProxyGreeter(GreeterInterface):
    def __init__(self, real_greeter):
        self.greeter = real_greeter

    def greet(self):
        # 1 Lookup greeter object on network and send request to call greet() method
        # 2 Check if the user is authorized to access
        # 3 Cache content
        print ("Proxy received the request.")
        return self.greeter.greet()


# Client
if __name__ == '__main__':
    print ("Direct Request =>")
    real = RealGreeter()
    print(real.greet())

    print ("Request via Proxy =>")
    proxy = ProxyGreeter(real)
    print(proxy.greet())
