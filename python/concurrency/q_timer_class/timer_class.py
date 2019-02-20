#timer class
import heapq
import threading
import datetime
import time


class Timer:
    def __init__(self):
        self.min_heap = []
        self.nmap = {}
        self.lock = threading.Lock()
        self.dispatch_thread = threading.Thread(target=self.start)

        '''
        # add the new thread job
        thread = threading.Thread(target=task)
        now = datetime.datetime.now()
        secs = now.second + now.minute * 60 + seconds
        heapq.heappush(self.min_heap, (secs, thread))
        '''

        # start the dispatch thread
        self.dispatch_thread.start()

    def add_tasks(self, seconds, task):
        thread = threading.Thread(target=task)
        now = datetime.datetime.now()
        secs = now.second + now.minute * 60 + seconds
        heapq.heappush(self.min_heap, (secs, thread))

    def start(self):
        print ("start", self.min_heap)
        while self.min_heap:
            now = datetime.datetime.now()
            secs, thread = self.min_heap[0]
            current = now.minute * 60 + now.second
            if current >= secs:
                heapq.heappop(self.min_heap) 
                thread.start()
                if self.min_heap:
                    secs, thread = self.min_heap[0]

            if secs-current > 0:
                print ("start thread sleep for ", secs-current, "seconds")
                time.sleep(secs-current)
        print ("finish", now)

    def cancel(self):
        pass

def func1():
    print ("starting task1 at", datetime.datetime.now())
    while True:
        time.sleep(1)

def func2():
    print ("starting task2 at", datetime.datetime.now())
    while True:
        time.sleep(1)

print ("start program", datetime.datetime.now())
t = Timer()
t.add_tasks(5, func1)
t.add_tasks(10, func2)
t.start()
