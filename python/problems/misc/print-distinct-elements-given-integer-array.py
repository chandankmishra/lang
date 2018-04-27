"""
Print All Distinct Elements of a given integer array
1.7
Given an integer array, print all distinct elements in array. The given array may contain duplicates and the output should print every element only once. The given array is not sorted.

Examples:

Input: arr[] = {12, 10, 9, 45, 2, 10, 10, 45}
Output: 12, 10, 9, 45, 2
"""
def printDistinct(arr):
    a = {}
    for i in arr:
        if i not in a:
            a[i] = 1
            print(i)


arr = ["chandan", "aadya", "veena", "aadya", "chandan", "saroj", "veena", "saroj"]
printDistinct(arr)

# arr = [10, 20, 30, 5, 23]
# maxval = 0

# for i in arr:
#     if i > maxval:
#         maxval = i
# print(maxval)
