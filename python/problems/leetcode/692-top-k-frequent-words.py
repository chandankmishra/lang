import collections
import heapq

k = 2
words = ["i", "love", "leetcode", "i", "love", "coding"]

# using sorting
count = collections.Counter(words)
candidates = list(count.keys())
sorted(candidates, key=lambda w: (-count[w], w))
print(candidates[:k])

# using heapq
count = collections.Counter(words)
heap = [(-freq, word) for word, freq in count.items()]
heapq.heapify(heap)
print([heapq.heappop(heap)[1] for _ in range(k)])

# third method using hash table and sorting
chmap = {}
for ch in words:
    chmap[ch] = 1 if ch not in chmap else chmap[ch] + 1

chmap = sorted(chmap.items(), key=lambda x: (-x[1], x[0]))
#chmap = sorted(sorted(chmap.items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
lst = []
for i in chmap:
    if k > 0:
        lst.append(i[0])
        k -= 1
print(lst)
