import threading
import time

lock = threading.Lock()
is_full = threading.Condition(lock)
is_empty = threading.Condition(lock)
count, read_idx, write_idx = 0, 0, 0
capacity = 10
arr = [0] * capacity


def producer():
    global count
    global write_idx
    while True:
        lock.acquire()
        while count == capacity:
            is_full.wait()

        write_idx = (write_idx + 1) % capacity
        arr[write_idx] = write_idx
        count += 1
        time.sleep(.1)
        print ("producer", count, write_idx)

        is_empty.notify()
        lock.release()


def consumer():
    global count
    global read_idx
    while True:
        lock.acquire()
        while count == 0:
            is_empty.wait()

        read_idx = (read_idx + 1) % capacity
        arr[read_idx] = read_idx
        count -= 1
        print ("consumer", count, read_idx)
        time.sleep(.1)

        is_full.notify()
        lock.release()


t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start()
t2.start()
t1.join()
t2.join()
