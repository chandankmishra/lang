# implement a message broadcaster (publisher subscriber)
# fix the threading/locking part!

import threading

class Publisher:
    def __init__(self):
        self.observers = []
        self.lock = threading.Lock()

    def register(self, observer):
        self.lock.acquire()
        if not observer in self.observers:
            self.observers.append(observer)
        self.lock.release()

    def unregister(self, observer):
        self.lock.acquire()
        if observer in self.observers:
            self.observers.remove(observer)
        self.lock.release()

    def notify_subscribers(self, update, msg):  # update_observers
        self.lock.acquire()
        for observer in self.observers:
            observer.update(update, msg)
        self.lock.release()

class Subscriber:
    def update(self, *args, **kwargs):
        pass

class Subscriber1(Subscriber):
    def update(self, update, msg):
        print ("subscriber1 received: {0} {1}".format(update, msg))

class Subscriber2(Subscriber):
    def update(self, update, msg):
        print ("subscriber2 received: {0} {1}".format(update, msg))

publisher = Publisher()

subs = []
subs.append(threading.Thread(target=publisher.register, args=(Subscriber1(), )))
subs.append(threading.Thread(target=publisher.register, args=(Subscriber2(), )))
for sub in subs:
    sub.start()

for i in range(10):
    publisher.notify_subscribers('update:', msg='msg-' + str(i))

for sub in subs:
    sub.join()
