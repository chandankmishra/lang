import threading
import time
import random

cv = threading.Condition()
count_max = 10
arr = [0] * count_max
read_idx, write_idx = 0, 0


def producer():
  """ Producer Thread """
  global write_idx
  while True:
    if (write_idx + 1) % 10 == read_idx:
        continue
    # Produce/write the data at write index
    print ("producer", write_idx)
    write_idx = (write_idx + 1) % count_max
    arr[write_idx] = "w"
    print ("producer", arr)


def consumer():
  """ Consumer Thread """
  global read_idx
  while True:
    if read_idx == write_idx:
        continue
    # Consume the data from read index
    print ("consumer", read_idx)
    read_idx = (read_idx + 1) % count_max
    arr[read_idx] = "r"
    print ("consumer",arr)


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
