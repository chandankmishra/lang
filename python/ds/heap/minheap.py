class MinHeap:
    ''' https://www.youtube.com/watch?v=t0Cq6tVNRBA&t=202s '''
    def __init__(self, size):
        self.capacity = size
        self.items = [0] * self.capacity
        self.size = 0

    # helper apis
    def _swap(self, idx1, idx2): self.items[idx1], self.items[idx2] = self.items[idx2], self.items[idx1]
    def _parentIndex(self, index): return (index - 1) // 2
    def _leftIndex(self, index): return (2 * index + 1)
    def _rightIndex(self, index): return (2 * index + 2)
    def _parent(self, index): return self.items[self._parentIndex(index)]
    def _right(self, index): return self.items[self._rightIndex(index)]
    def _left(self, index): return self.items[self._leftIndex(index)]
    def _hasParent(self, index): return self._parentIndex(index) >= 0
    def _hasRight(self, index): return self._rightIndex(index) < self.size
    def _hasLeft(self, index): return self._leftIndex(index) < self.size
    def _isEmpty(self): return True if self.size == 0 else False
    def _isFull(self): return True if self.size and self.size == self.capacity else False

    def _heapifyUp(self):
        index = self.size - 1
        while (self._hasParent(index)  and self._parent(index) > self.items[index]): #compare the values
            self._swap(self._parentIndex(index), index) # swap the value @index
            index = self._parentIndex(index)

    def _heapifyDown(self):
        index = 0
        while self._hasLeft(index):
            # get the child index with the smaller value
            smallidx = self._leftIndex(index)
            if self._left(index) < self._right(index): smallidx = self._rightIndex(index)
            if self.items[index] < self.items[smallidx]:  break
            self._swap(index, smallidx)
            index = smallidx

    # operations which needed by the priority queue
    def insertKey(self, item):
        '''IMP: Add the key by value not index '''
        if self._isFull(): raise KeyError("Heap is already full.")

        self.items[self.size] = item
        self.size += 1
        self._heapifyUp()
        print ("added ", item)

    def popmin(self):
        '''IMP Removes and return the minimum value '''
        if _isEmpty(): raise KeyError("Heap is already empty.")

        tmp = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self._heapifyDown()
        return tmp

    def decreaseKey(self, index, val):
        '''IMP Decrease the key @index by value (val) '''
        self.items[index] = val
        while index != 0 and self._parent(index) > self.items[index]:
            self._swap(index, self._parentIndex(index))
            index = self._parentIndex(index)

    def top(self):
        return self.items[0]

    def deleteKey(self, index):
        ''' Delete the key by index not value '''
        print ("deleted ", index)
        self.decreaseKey(index, float("-inf"))
        self.popmin()


def main():
    h = MinHeap(11)
    h.insertKey(3)
    h.insertKey(2)
    print("top", h.top())
    print("popmin", h.popmin())
    print("top", h.top())
    h.insertKey(15)
    h.insertKey(5)
    h.insertKey(4)
    h.insertKey(45)
    print("popmin", h.popmin())
    print("top", h.top())
    h.decreaseKey(2, 1)
    print("top", h.top())
    h.deleteKey(0)
    print("top", h.top())

if __name__ == "__main__":
    main()
