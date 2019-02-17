'''
Implemented a bounded hash set with fixed size.
APIs:
    add(val)
    remove(val)
DS:
'''
class BHS_Semaphore:
    def __init__(capacity):
        self.hs = set() # hashset
        self.sem = threading.semaphore(capacity)
        self.m = threading.mutex()

    def add(val):
        self.sem.wait() 
        self.m.acquire()
        if val not in self.hs:
           sem.release() 
        else:
           self.hs.add(val):
        self.m.release()

    def remove(val):
        self.m.acquire()
        if val in self.hs:
            self.hs.remove(val):
            sem.signal()
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
           self.cv_full.wait()

        self.hs.add(val):

        self.cv_empty.notify()
        self.m.release()

    def remove(val):
        self.m.acquire()
        while len(self.hs) == 0:
            cv_empty.wait()

        self.hs.remove(val):

        self.cv_full.notify()
        self.m.release()
