# implement read write map using read write lock

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
        self.writer += 1  # to fix writer starvation
        while (self.reading or self.writing):
            self.write_cv.wait()
        self.writing = 1
        # self.write_cv.release()

    def write_unlock(self):
        # self.write_cv.acquire()
        self.writing = 0
        self.writer -= 1  # to fix writer starvation
        self.read_cv.notify_all()
        self.write_cv.release()


class RwMap:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.size = 0
        self.main_lock = RwLockFair()
        self.rw_list = [(RwLockFair(), {}) for _ in range(self.capacity)]

    def get(self, key):
        k = key % self.capacity
        self.main_lock.read_lock()
        val = self.rw_list[k]
        bucket_map = val[1]
        rw_lock = val[0]
        rw_lock.read_lock()
        rval = None
        if key in bucket_map:
            rval = bucket_map[key]
        rw_lock.read_unlock()
        self.main_lock.read_unlock()
        return rval

    def put(self, key, data):
        k = key % self.capacity
        self.main_lock.read_lock()
        val = self.rw_list[k]
        bucket_map = val[1]
        rw_lock = val[0]
        rw_lock.write_lock()
        bucket_map[key] = data
        self.size += 1
        rw_lock.write_unlock()
        self.main_lock.read_unlock()

    def resize(self, new_capacity):
        self.main_lock.write_lock()
        new_list = [(RwLockFair(), {}) for _ in range(new_capacity)]
        for lock, old_rw_map in self.rw_list:
            for key in old_rw_map:
                k = key % new_capacity
                new_rw_map = new_list[k][1]
                new_rw_map[key] = old_rw_map[key]
        self.rw_list = new_list
        self.main_lock.write_unlock()

    def display(self):
        for i, val in enumerate(self.rw_list):
            print (i, val)


def main():
    rw_map = RwMap()
    rw_map.put(1, "chandan")
    rw_map.put(2, "veena")
    rw_map.display()
    rw_map.resize(10)
    rw_map.display()
    # print (rw_map.get(1))
    # print (rw_map.get(2))
    # print (rw_map.size)


if __name__ == "__main__":
    main()