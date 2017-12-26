class MinHeap:
    def __init__(self, size):
        self.capacity = size
        self.items = [0] * self.capacity
        self.size = 0

    def swap(self, idx1, idx2):
        tmp = self.items[idx1]
        self.items[idx1] = self.items[idx2]
        self.items[idx2] = tmp

    def parent(self, index):
        return index // 2

    def heapifyUp(self):
        i = self.size - 1
        while (i != 0 and self.items[self.parent(i)] > self.items[i]):
            i = self.parent(i)

    def insertKey(self, item):
        if self.size == self.capacity:
            return
        self.items[self.size] = item
        self.size += 1
        self.heapifyUp()

    def deleteKey(self, item):
        print (item)

    def extractMin(self):
        print ("extractMin")

    def getMin(self):
        return self.items[0]

    def decreaseKey(self, index, val):
        print ("decreaseKey")


def main():
    h = MinHeap(11)
    h.insertKey(3)
    h.insertKey(2)
    h.deleteKey(1)
    h.insertKey(15)
    h.insertKey(5)
    h.insertKey(4)
    h.insertKey(45)
    print(h.extractMin())
    print(h.getMin())
    h.decreaseKey(2, 1)
    print(h.getMin())


if __name__ == "__main__":
    main()
