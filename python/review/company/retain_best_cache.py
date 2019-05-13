'''
Design Retain best cache
- Get (key) - returns value V from the cache if it exists. If it does not
  exist then read from underlying storage using API dsGet(key).
- If cache exceeds max size then evict the lowest rank element from the
  cache. Each rank can be found value from only. rank = value.getRank()

PQ <Rank, Key> => PQ<Rank, set(keys)> => TreeMap<Rank, set(keys)>
HashMap <K,V>

TimeComplexity log(R)
'''

class RBC:
    def __init__(self, capacity):
        self.hashmap = {}
        self.pq = []
        self.capacity = capcity
        self.size = size

    def get(key):
        if key in hashmap:
            value = hashmap[key]
            return value

        value = dsGet(key)
        rank = value.getRank()
        if self.size == self.capacity:
            if rank < self.pq[0][0]:
                return value
            r, k = heapq.heappop(heap)
            self.pa.pop(k)
        else:
            self.size += 1
        heapq.heappush(self.pq, (rank, key))
        hashmap[key] = value
        return value
 
obj = RBC(10)
print (obj.get())

