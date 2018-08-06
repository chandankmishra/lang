import heapq

class PriorityQueue:
    '''Variant of Queue that retrieves open entries in priority order (lowest first).
    Entries are typically tuples of the form:  (priority number, data).
    '''

    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def put(self, item, priority):
        heapq.heappush(self.queue, (priority, item))

    def get(self):
        _, item = heapq.heappop(self.queue)
        return item

    def peek(self):
        return self.queue[0]


def main():
    pq = PriorityQueue()
    pq.put('a', 1)
    pq.put('b', 2)
    pq.put('c', 0)
    pq.put('d', 4)
    pq.put('e', 3)

    print (pq.get())
    print (pq.get())
    print (pq.get())

if __name__ == "__main__":
    main()

