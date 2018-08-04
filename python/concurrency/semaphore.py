import threading
import time
import random

semaphore = threading.Semaphore(0)


def consumer():
    while True:
        print ("consumer is waiting...")
        semaphore.acquire()
        print (f"consumer notify: consumed item {item}")


def producer():
    global item
    for i in range(10):
        time.sleep(1)
        item = random.randint(0, 10000)
        print ("producer notify: produced item {0}".format(item))
        semaphore.release()


def main():
    t0 = time.time()
    thread1 = threading.Thread(target=consumer)
    thread2 = threading.Thread(target=producer)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    t1 = time.time()

    print("Execution Time {}".format(t1 - t0))


if __name__ == '__main__':
    main()
