import threading
import time
import random

lock = threading.Lock()
cv_full = threading.Condition(lock)
cv_empty = threading.Condition(lock)

is_even = False
count_max = 10
arr = [0] * count_max
read_idx, write_idx, count = 0, 0, 0


def producer():
  """ Thread A will print odd numbers 1,3,...99 """
  global arr
  while True:
    global write_idx
    global count
    lock.acquire()
    while count == count_max:
      cv_full.wait()
    write_idx = (write_idx + 1) % count_max
    arr[write_idx] = write_idx
    count += 1
    print ("producer", count)
    time.sleep(0.1)
    cv_empty.notify()
    lock.release()


def consumer():
  """ Thread B will print even numbers 2,4,..100 """
  global arr
  while True:
    global read_idx
    global count
    lock.acquire()
    while count == 0:
      cv_empty.wait()
    read_idx = (read_idx + 1) % count_max
    arr[read_idx] = 0
    count -= 1
    print ("consumer", count)
    time.sleep(0.1)
    cv_full.notify()
    lock.release()


def main():
  t0 = time.time()
  thread1 = threading.Thread(target=producer)
  thread2 = threading.Thread(target=consumer)

  thread1.start()
  thread2.start()

  thread1.join()
  thread2.join()

  t1 = time.time()

  print("Execution Time {}".format(t1 - t0))


if __name__ == '__main__':
  main()
