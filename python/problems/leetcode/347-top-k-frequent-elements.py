def left(index): return (2 * index + 1)


def right(index): return (left(index) + 1)


def swap(nums, idx1, idx2): nums[idx1], nums[idx2] = nums[idx2], nums[idx1]


def heapifyDown(nums, index, size):
    while left(index) < size:
        largest = left(index)

        # right child exists and is larger than left child
        if (right(index) < size) and (nums[left(index)] < nums[right(index)]):
            largest = right(index)

        # right child is larger than parent
        if nums[largest] <= nums[index]:
            break
        else:
            swap(nums, index, largest)
        # move down to largest child
        index = largest


def extractMax(nums, size):
    tmp = nums[0]
    nums[0] = nums[size - 1]
    heapifyDown(nums, 0, size)
    return tmp


k = 3
nums = [12, 11, 13, 5, 6, 7, 20, 21, 26, 22]

size = len(nums)
leastParent = size // 2 - 1
for i in range(leastParent, -1, -1):
    heapifyDown(nums, i, size)
lst = []
for i in range(k):
    lst.append(extractMax(nums, size - i))
print (lst)
