import threading
import time

'''
Implemented a bounded hash set with fixed size.
APIs:
    add(val)
    remove(val)
DS:
'''
class BHS_Semaphore:
    def __init__(self, capacity):
        self.hs = set() # hashset
        self.sem = threading.Semaphore(capacity)
        self.m = threading.RLock()

    def add(self, val):
        self.sem.acquire() 
        self.m.acquire()
        if val in self.hs:
           self.sem.release() 
        else:
           self.hs.add(val)

        self.m.release()

    def remove(self, val):
        self.m.acquire()
        if val in self.hs:
            self.hs.remove(val)
            self.sem.release()
        self.m.release()


class BHS_CV:
    def __init__(capacity):
        self.hs = set() # hashset
        self.m = threading.mutex()
        self.cv_full = threading.Condition(self.m)
        self.cv_empty = threading.Condition(self.m)

    def add(val):
        self.m.acquire()
        while len(self.hs) >= self.capacity:
            print ("can not produce wait..", val)
            self.cv_full.wait()

        self.hs.add(val)

        self.cv_empty.notify()
        self.m.release()

    def remove(val):
        self.m.acquire()
        while len(self.hs) == 0:
            cv_empty.wait()

        self.hs.remove(val)

        self.cv_full.notify()
        self.m.release()

def producer(bhs):
    while True:
        for val in [1,2,3,4,4,5,5,6,7,8,9,10]:
            bhs.add(val)
            print ("producer", bhs.hs)

def consumer(bhs):
    while True:
        for val in [1,2,3,4,4,5,5,6,7,8,9,10]:
            bhs.remove(val)
            print ("consumer", bhs.hs)
        time.sleep(1)

bhs = BHS_Semaphore(5)
thread1 = threading.Thread(target=producer, args=(bhs,))
thread2 = threading.Thread(target=consumer, args=(bhs,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print ("DONE")
