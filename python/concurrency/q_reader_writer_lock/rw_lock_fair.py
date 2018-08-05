import threading
import time
import random


class RwLockFair:
    """ Read write lock giving fairness to both read and write. """
    def __init__(self):
        self.lock = threading.Lock()
        self.read_cv = threading.Condition(self.lock)
        self.write_cv = threading.Condition(self.lock)
        self.writer = 0
        self.writing = 0
        self.reading = 0

    def read_lock(self):
        self.read_cv.acquire()
        while self.writer:
            self.read_cv.wait()
        self.reading += 1
        self.read_cv.release()

    def read_unlock(self):
        self.read_cv.acquire()
        self.reading -= 1
        self.write_cv.notify_all()
        self.read_cv.release()

    def write_lock(self):
        self.write_cv.acquire()
        self.writer += 1 # to fix writer starvation
        while (self.reading or self.writing):
            self.write_cv.wait()
        self.writing = 1
        #self.write_cv.release()

    def write_unlock(self):
        #self.write_cv.acquire()
        self.writing = 0
        self.writer -= 1 # to fix writer starvation
        self.read_cv.notify_all()
        self.write_cv.release()

################ application code ##################
item = 0
def read(thr_no, rwlock):
    while True:
        rwlock.read_lock()
        print (f"reader {thr_no} notify: consumed item {item}")
        rwlock.read_unlock()
        time.sleep(0.2)

def write(thr_no, rwlock):
    global item
    while True:
        rwlock.write_lock();
        item = random.randint(1000, 10000)
        print (f"writer {thr_no} notify: produced item {item}")
        rwlock.write_unlock();
        time.sleep(0.2)

def main():
    t0 = time.time()
    rwlock = RwLockFair()
    threads = []
    read_threads = 20
    write_threads = 5

    for i in range(write_threads):
        threads.append(threading.Thread(target=write, args=(i,rwlock)))

    for i in range(read_threads):
        threads.append(threading.Thread(target=read, args=(i,rwlock)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    t1 = time.time()

    print("Execution Time {}".format(t1 - t0))


if __name__ == '__main__':
    main()
