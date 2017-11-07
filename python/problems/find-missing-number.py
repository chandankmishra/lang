"""
Given a array of 'n' elements with numbers in the range of 1-n
There is exactly 1 number missing that we need to find
"""

arr = [1, 2, 3, 4, 5, 7]

# Method 1: Get the sum using n * (n+1)/ 2 and subtract the sum of the array
n = len(arr) + 1
range_sum = n * (n + 1) // 2

sum = 0
for i in arr:
    sum = sum + i

print (range_sum - sum)

# Method 2: Add the array element in a set and then just run the loop for n element and if the element is not in the set then print it and break from the loop.
data = set()
for i in arr:
    data.add(i)

for i in range(1, n + 1):
    if i not in data:
        print (i)
        break
