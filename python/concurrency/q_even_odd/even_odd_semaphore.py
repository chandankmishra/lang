import threading
import time
import random

even_semaphore = threading.Semaphore(0)
odd_semaphore = threading.Semaphore(1)


def even_print():
    for i in range(2, 101):
        even_semaphore.acquire()
        print ("even_print", i)
        odd_semaphore.release()


def odd_print():
    for i in range(1, 101):
        odd_semaphore.acquire()
        print ("odd_print ", i)
        even_semaphore.release()


def main():
    t0 = time.time()
    thread1 = threading.Thread(target=even_print)
    thread2 = threading.Thread(target=odd_print)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    t1 = time.time()

    print("Execution Time {}".format(t1 - t0))


if __name__ == '__main__':
    main()
