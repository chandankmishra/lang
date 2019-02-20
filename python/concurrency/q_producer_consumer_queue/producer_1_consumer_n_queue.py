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
    print (f'producer notify: item {item} is added to queue')
    time.sleep(1)


def consumer(thread_id):
  """ Consumer: Take the item out of the queue and notify that task is done using task_done() """
  while True:
    item = queue.get()
    print (f'consumer {thread_id} notify: item {item} is popped from queue')
    queue.task_done()


def main():
    t0 = time.time()
    threads=[]
    threads.append(threading.Thread(target=producer))
    for i in range(3):
        threads.append(threading.Thread(target=consumer, args=(i,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    t1 = time.time()

    print("Execution Time {}".format(t1 - t0))


if __name__ == '__main__':
    main()
