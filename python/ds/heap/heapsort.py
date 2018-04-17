def left(index): return (2 * index + 1)


def right(index): return (left(index) + 1)


def swap(items, idx1, idx2): items[idx1], items[idx2] = items[idx2], items[idx1]


def heapsort(items):
    # convert items to heap
    n = len(items)
    leastParent = n // 2 - 1
    for i in range(leastParent, -1, -1):
        heapifyDown(items, i, n)
    print (items)

    # flatten heap into sorted array
    for i in range(n - 1, -1, -1):
        if items[0] > items[i]:
            swap(items, 0, i)
            heapifyDown(items, 0, i)


def heapifyDown(items, index, size):
    while left(index) < size:
        largest = left(index)

        # right child exists and is larger than left child
        if (right(index) < size) and (items[left(index)] < items[right(index)]):
            largest = right(index)

        # right child is larger than parent
        if items[largest] <= items[index]:
            break
        else:
            swap(items, index, largest)
        # move down to largest child
        index = largest


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7, 20, 21, 26, 22]
heapsort(arr)
print (arr)
