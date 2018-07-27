class Singleton:
    __instance = None

    def __new__(cls, val=None):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        Singleton.__instance.val = val
        return Singleton.__instance


if __name__ == '__main__':
    x1 = Singleton()
    x1.val = 'burger'
    print (x1.val)

    x2 = Singleton()
    x2.val = 'chips'
    print (x2.val)
    print (x1.val)

# Python Modules are singletons
