import threading
import time
import random

cv = threading.Condition()
counter = 0
# lock = threading.Lock()


def workerA():
  global counter
  while counter < 100:
    cv.acquire()
    while counter % 2 != 0:
      cv.wait()
    if counter < 100:
      counter += 1
      print ("A", counter)
    cv.notify()
    cv.release()


def workerB():
  global counter
  while counter < 100:
    cv.acquire()
    while counter % 2 == 0:
      cv.wait()
    if counter < 100:
      counter += 1
      print ("B", counter)
    cv.notify()
    cv.release()


def main():
  t0 = time.time()
  thread1 = threading.Thread(target=workerA)
  thread2 = threading.Thread(target=workerB)

  thread1.start()
  thread2.start()

  thread1.join()
  thread2.join()

  t1 = time.time()

  print("Execution Time {}".format(t1 - t0))


if __name__ == '__main__':
  main()
