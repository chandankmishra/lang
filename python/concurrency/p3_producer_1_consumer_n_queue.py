import threading
import queue
import time
import random

queue = queue.Queue()


def producer():
  """ Producer: Add the item in the Queue """
  for i in range(10):
    item = random.randint(0, 256)
    queue.put(item)
    print (f'Producer notify: item {item} is added to queue')
    time.sleep(1)


def consumer1():
  """ Consumer: Take the item out of the queue and notify that task is done using task_done() """
  while True:
    item = queue.get()
    print (f'consumer1 notify: item {item} is popped from queue')
    queue.task_done()


def consumer2():
  """ Consumer: Take the item out of the queue and notify that task is done using task_done() """
  while True:
    item = queue.get()
    print (f'consumer2 notify: item {item} is popped from queue')
    queue.task_done()


def main():
  t0 = time.time()
  thread1 = threading.Thread(target=producer)
  thread2 = threading.Thread(target=consumer1)
  thread3 = threading.Thread(target=consumer2)

  thread1.start()
  thread2.start()
  thread3.start()

  thread1.join()
  thread2.join()
  thread3.join()

  t1 = time.time()

  print("Execution Time {}".format(t1 - t0))


if __name__ == '__main__':
  main()
