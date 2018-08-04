import threading
import time
import random

readers = 0
resource_lock = threading.Lock()
readers_lock = threading.Lock()
item = 0


def write_lock():
    resource_lock.acquire()


def write_unlock():
    resource_lock.release()


def read_lock():
    global readers
    readers_lock.acquire()
    try:
        readers += 1
        if readers == 1:
            resource_lock.acquire()
    finally:
        readers_lock.release()


def read_unlock():
    global readers
    readers_lock.acquire()
    try:
        readers -= 1
        if readers == 0:
            resource_lock.release()
    finally:
        readers_lock.release()


def reader1():
    # while True:
    for i in range(10):
        print ("reader1 is waiting...")
        try:
            read_lock()
            print (f"reader1 notify: consumed item {item}")
        finally:
            read_unlock()


def reader2():
    while True:
        # for i in range(10):
        print ("reader2 is waiting...")
        try:
            read_lock()
            print (f"reader2 notify: consumed item {item}")
        finally:
            read_unlock()


def writer():
    global item
    for i in range(10):
        # time.sleep(1)
        try:
            write_lock()
            item = random.randint(0, 10000)
            print ("producer notify: produced item {0}".format(item))
        finally:
            write_unlock()


def main():
    t0 = time.time()
    thread1 = threading.Thread(target=reader1)
    # thread2 = threading.Thread(target=reader2)
    thread3 = threading.Thread(target=writer)

    thread1.start()
    # thread2.start()
    thread3.start()

    thread1.join()
    # thread2.join()
    thread3.join()

    t1 = time.time()

    print("Execution Time {}".format(t1 - t0))


if __name__ == '__main__':
    main()
