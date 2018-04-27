"""
370. Range Addition

Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:

Given:
    length = 5,
    updates = [
        [1,  3,  2],
        [2,  4,  3],
        [0,  2, -2]
    ]

Output:
    [-2, 0, 3, 5, 3]
Explanation:

Initial state:
[ 0, 0, 0, 0, 0 ]

After applying operation [1, 3, 2]:
[ 0, 2, 2, 2, 0 ]

After applying operation [2, 4, 3]:
[ 0, 2, 5, 5, 3 ]

After applying operation [0, 2, -2]:
[-2, 0, 3, 5, 3 ]
"""


def getModifiedArray(length, updates):
    """
    :type length: int
    :type updates: List[List[int]]
    :rtype: List[int]
    """
    n = [0 for i in range(0, length + 1)]

    for upd in updates:
        n[upd[0]] += upd[2]
        n[upd[1] + 1] -= upd[2]

    for i in range(1, length + 1):
        n[i] += n[i - 1]
    n.pop()
    return n


u = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
print(getModifiedArray(5, u))

# slow solution
# n = [0 for i in range(0, length)]
# for upd in updates:
#     for j in range(upd[0], upd[1] + 1):
#         n[j] += upd[2]

# return n
