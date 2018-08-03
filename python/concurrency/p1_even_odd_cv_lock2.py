import threading
import time
import random

cv = threading.Condition()
is_even = False


def odd_print():
  """ Thread A will print odd numbers 1,3,...99 """
  global is_even
  for count in range(1, 101, 2):
    cv.acquire()
    while is_even is True:
      cv.wait()
    print ("odd_print ", count)
    is_even = True
    cv.notify()
    cv.release()


def even_print():
  """ Thread B will print even numbers 2,4,..100 """
  global is_even
  for count in range(2, 101, 2):
    cv.acquire()
    while is_even is False:
      cv.wait()
    print ("even_print", count)
    is_even = False
    cv.notify()
    cv.release()


def main():
  t0 = time.time()
  thread1 = threading.Thread(target=odd_print)
  thread2 = threading.Thread(target=even_print)

  thread1.start()
  thread2.start()

  thread1.join()
  thread2.join()

  t1 = time.time()

  print("Execution Time {}".format(t1 - t0))


if __name__ == '__main__':
  main()
