from collections import deque


class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = deque()

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue) == self.size:
            self.queue.popleft()

        self.queue.append(val)
        return sum(self.queue) / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
size = 3
obj = MovingAverage(size)
print (obj.next(1))
print (obj.next(10))
print (obj.next(3))
print (obj.next(5))
