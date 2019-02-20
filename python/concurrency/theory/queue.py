'''A multi-producer, multi-consumer queue.
https://github.com/python/cpython/blob/3.7/Lib/queue.py
'''

import threading
from collections import deque
from heapq import heappush, heappop
from time import monotonic as time

class Full(Exception):
    'Exception raised by Queue.put(block=0)/put_nowait().'
    pass

class Queue:
    def __init__(self, maxsize=0):
        self.maxsize = maxsize
        self.queue = deque()
        self.mutex = threading.Lock()
        self.not_empty = threading.Condition(self.mutex)
        self.not_full = threading.Condition(self.mutex)
        self.all_tasks_done = threading.Condition(self.mutex)
        self.unfinished_tasks = 0

    def task_done(self):
        with self.all_tasks_done:
            unfinished = self.unfinished_tasks - 1
            if unfinished <= 0:
                if unfinished < 0:
                    raise ValueError('task_done() called too many times')
                self.all_tasks_done.notify_all()
            self.unfinished_tasks = unfinished

    def join(self):
        with self.all_tasks_done:
            while self.unfinished_tasks:
                self.all_tasks_done.wait()

    def qsize(self):
        with self.mutex:
            return self._qsize()

    def empty(self):
        with self.mutex:
            return not self._qsize()

    def full(self):
        with self.mutex:
            return 0 < self.maxsize <= self._qsize()

    def put(self, item, block=True, timeout=None):
        with self.not_full:
            if self.maxsize > 0:
                while self._qsize() >= self.maxsize:
                    self.not_full.wait()
            self.queue.append(item)
            self.unfinished_tasks += 1
            self.not_empty.notify()

    def get(self, block=True, timeout=None):
        with self.not_empty:
            while not self._qsize():
                self.not_empty.wait()
            item = self.queue.popleft()
            self.not_full.notify()
            return item

    def _qsize(self):
        return len(self.queue)

