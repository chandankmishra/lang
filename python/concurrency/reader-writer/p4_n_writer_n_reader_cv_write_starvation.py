import threading
import time
import random

readers = 0
lock = threading.Lock()
read_cv = threading.Condition(lock)
write_cv = threading.Condition(lock)
item = 0
writing = 0
reading = 0

def read(thr_no):
    global reading
    while True:
        print (f"reader {thr_no} is waiting...")
        read_cv.acquire()
        while writing:
            read_cv.wait()

        reading += 1
        read_cv.release()

        print (f"reader {thr_no} notify: consumed item {item}")

        read_cv.acquire()
        reading -= 1
        write_cv.notify()
        read_cv.release()
        time.sleep(0.1)

def write(thr_no):
    global item
    global writing
    while True:
        print (f"writer {thr_no} is waiting...")
        write_cv.acquire()

        while (reading or writing):
            write_cv.wait()
        writing = 1

        item = random.randint(1000, 10000)
        print (f"writer {thr_no} notify: produced item {item}")

        writing = 0
        read_cv.notify_all()
        write_cv.release()
        time.sleep(0.1)

def main():
    t0 = time.time()
    threads = []
    for i in range(3):
        threads.append(threading.Thread(target=write, args=(i,)))

    for i in range(20):
        threads.append(threading.Thread(target=read, args=(i,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    t1 = time.time()

    print("Execution Time {}".format(t1 - t0))


if __name__ == '__main__':
    main()
