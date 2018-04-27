"""
Convert an array to reduced form | Set 1 (Simple and Hashing)
Given an array with n distinct elements, convert the given array to a form where all elements are in range from 0 to n-1. The order of elements is same, i.e., 0 is placed in place of smallest element, 1 is placed for second smallest element, … n-1 is placed for largest element.

Input:  arr[] = {10, 40, 20}
Output: arr[] = {0, 2, 1}
"""
arr = [10, 40, 20]
arr2 = sorted(arr.copy())

data = {} #empty dict
j = 0
for i in arr2:
    data[i] = j     #initialize dict with key as values and value as index in array
    j = j + 1

j = 0
for i in arr:
    arr[j] = data[i]
    j = j + 1

print(arr)
