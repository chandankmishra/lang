import threading
import queue
import time
import random
import collections


class RateLimiter:
    def __init__(self):
        self.maxsize = 10
        self.size = 0
        self.interval = 1
        self.rl_queue = collections.deque()
        self.lock = threading.Lock()
        self.client_cv = threading.Condition(self.lock)
        self.server_cv = threading.Condition(self.lock)

    def request_handler(self, thread_id, item):
        cur_time = time.time()
        self.client_cv.acquire()
        if self.size < self.maxsize:
            self.rl_queue.append((item, cur_time))
            print("{0}/{1} client {2} notify: item {3} is added to "
                  "queue".format(time.time(), self.size, thread_id, item))
            self.size += 1
        else:
            stored_item, stored_time = self.rl_queue[0]
            if cur_time - stored_time > 1:
                self.rl_queue.popleft()
                self.rl_queue.append((item, cur_time))
            else:
                print("{0}/{1} client {2} request dropped for "
                      "{3}".format(time.time(), self.size, thread_id, item))
                self.client_cv.wait()
        self.server_cv.notify_all()
        self.client_cv.release()

    def server(self, thread_id):
        while True:
            self.server_cv.acquire()
            while self.size == 0:
                self.server_cv.wait()    
            item, cur_time = self.rl_queue.popleft()
            print("{0}/{1} server {2} notify: item {3} is popped "
                  "from queue".format(time.time(), self.size, thread_id, item))
            self.size -= 1
            self.client_cv.notify_all()    
            self.server_cv.release()
            time.sleep(0.1)

    def client_request(self, thread_id):
        for i in range(100):
            item = random.randint(0, 256)
            self.request_handler(thread_id, item)

def main():
    t0 = time.time()
    threads = []
    rl = RateLimiter()

    for i in range(2):
        threads.append(threading.Thread(target=rl.server, args=(i,)))

    for i in range(5):
        threads.append(threading.Thread(target=rl.client_request, args=(i,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    t1 = time.time()

    print("Execution Time {}".format(t1 - t0))


if __name__ == '__main__':
    main()
