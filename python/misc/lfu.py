# https://leetcode.com/problems/lfu-cache/discuss/207673/Python-concise-solution-**detailed**-explanation%3A-Two-dict-%2B-Doubly-linked-list

import collections


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DList:
    def __init__(self):
        self._dummy = Node(None, None)  # dummy node
        self._dummy.next = self._dummy.prev = self._dummy
        self._size = 0

    def __len__(self):
        return self._size

    def append(self, node):
        node.next = self._dummy.next
        node.prev = self._dummy
        node.next.prev = node
        self._dummy.next = node
        self._size += 1

    def pop(self, node=None):
        if self._size == 0:
            return None
        if not node:
            node = self._dummy.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self._size = 0
        self._capacity = capacity
        self._node_map = dict()  # key: Node
        self._freq_map = collections.defaultdict(DList)  # freq: list of nodes
        self._minfreq = 0

    def _update(self, node):
        freq = node.freq
        self._freq_map[freq].pop(node)
        if self._minfreq == freq and not self._freq_map[freq]:
            self._minfreq += 1

        node.freq += 1
        freq = node.freq
        self._freq_map[freq].append(node)

    def get(self, key: int) -> int:
        if key not in self._node_map:
            return -1

        node = self._node_map[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return

        if key in self._node_map:
            node = self._node_map[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                node = self._freq_map[self._minfreq].pop()
                del self._node_map[node.key]
                self._size -= 1

            node = Node(key, value)
            self._node_map[key] = node
            self._freq_map[1].append(node)
            self._minfreq = 1
            self._size += 1


# Your LFUCache object will be instantiated and called as such:
capacity = 2
cache = LFUCache(capacity)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))       # returns 1
cache.put(3, 3)           # evicts key 2
print(cache.get(2))       # returns -1 (not found)
print(cache.get(3))       # returns 3.
cache.put(4, 4)           # evicts key 1.
print(cache.get(1))       # returns -1 (not found)
print(cache.get(3))       # returns 3
print(cache.get(4))       # returns 4


'''

["LRUCache","put","put","get","put","get","put","get","get","get"]
[[1],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

'''
