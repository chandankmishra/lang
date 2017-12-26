class MinHeap:
    def __init__(self, size):
        self.capacity = size
        self.items = [0] * self.capacity
        self.size = 0

    def swap(self, idx1, idx2):
        self.items[idx1], self.items[idx2] = self.items[idx2], self.items[idx1]

    def parent(self, index):
        return index // 2

    def left(self, index):
        return (2 * index + 1)

    def right(self, index):
        return (2 * index + 2)

    def heapifyUp(self):
        i = self.size - 1
        pi = self.parent(i)
        while (i != 0 and self.items[pi] > self.items[i]):
            self.swap(pi, i)
            i = pi

    def heapifyDown(self):
        i = 0
        while self.left(i) < self.size:
            smallidx = self.left(i)

            if self.items[self.right(i)] < self.items[self.left(i)]:
                smallidx = self.right(i)
            if self.items[i] < self.items[smallidx]:
                break
            else:
                self.swap(i, smallidx)
            i = smallidx

    def insertKey(self, item):
        if self.size == self.capacity:
            return
        self.items[self.size] = item
        self.size += 1
        self.heapifyUp()

    def deleteKey(self, index):
        self.decreaseKey(index, float("-inf"))
        self.extractMin()

    def extractMin(self):
        tmp = self.items[0]
        self.items[0] = self.items[self.size - 1]
        #self.items[self.size - 1] = 0
        self.size -= 1
        self.heapifyDown()
        return tmp

    def getMin(self):
        return self.items[0]

    def decreaseKey(self, index, val):
        self.items[index] = val
        while index != 0 and self.items[self.parent(index)] > self.items[index]:
            self.swap(index, self.parent(index))
            index = self.parent(index)


def main():
    h = MinHeap(11)
    h.insertKey(3)
    h.insertKey(2)
    h.deleteKey(1)
    h.insertKey(15)
    h.insertKey(5)
    h.insertKey(4)
    h.insertKey(45)
    print("extractMin", h.extractMin())
    print("getMin", h.getMin())
    h.decreaseKey(2, 1)
    print("getMin", h.getMin())


if __name__ == "__main__":
    main()
