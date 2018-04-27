"""
Find missing elements of a range
Given an array arr[0..n-1] of distinct elements and a range [low, high], find all numbers that are in range, but not in array. The missing elements should be printed in sorted order.

Examples:

Input: arr[] = {10, 12, 11, 15},
       low = 10, hight = 15
Output: 13, 14
"""
arr = [10, 12, 11, 15]
low = 10
high = 15

data = {}       # define empty dict
data1 = set()   # define empty set
for i in arr:
    data[i] = 1 #using dictionary
    data1.add(i)    #using set

for i in range(low, high):
    if i not in data:
        print (i)

for i in range(low, high):
    if i not in data1:
        print (i)
