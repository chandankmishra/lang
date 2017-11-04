"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

# function to check for the given sum in the array


def returnIndexPair(arr, sum):
    print ("A =", arr, "n=", sum)
    data = {}
    j = 1
    for i in arr:
        temp = sum - i
        if (temp in data):
            return [data[temp] - 1, j - 1]
        data[i] = j
        j = j + 1
    return []


A = [3, 3]
n = 6
print(returnIndexPair(A, n))

A = [3, 2, 4]
n = 6
print(returnIndexPair(A, n))

A = [1, 4, 45, 6, 10, -8]
n = 16
print(returnIndexPair(A, n))

A = [1, 2, 4]
n = 6
print(returnIndexPair(A, n))

A = [-3, 4, 3, 90]
n = 0
print(returnIndexPair(A, n))


def twoSum(nums, target):
    data = {}
    j = 0
    for i in nums:
        data[i] = j
        j = j + 1

    j = 0
    for i in nums:
        if target - i in data:
            if data[i] != data[target - i]:
                return [j, data[target - i]]
        j = j + 1
    return []


# arr = [2, 7, 11, 15]
# target = 26
# print (twoSum(arr, target))

# arr = [3, 2, 4]
# target = 6
# print (twoSum(arr, target))

# # This testcase is not passing!!!
# arr = [3, 3]
# target = 6
# print (twoSum(arr, target))
