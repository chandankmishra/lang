"""
566. Reshape the Matrix

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.
You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.
The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
Output:
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
Output:
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
"""


def matrixReshape(nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    if r * c != len(nums) * len(nums[0]):
        #print("orignal matrix:")
        return nums

    #print("new matrix:")
    l = [[0] * c for i in range(r)]

    r2 = 0
    c2 = 0
    for r1 in range(0, len(nums)):
        for c1 in range(0, len(nums[r1])):
            #print (r1, c1, r2, c2)
            l[r2][c2] = nums[r1][c1]
            c2 += 1
            if c2 % c == 0:
                c2 = 0
                r2 += 1

    return l


m = [[1, 2], [3, 4]]
print(matrixReshape(m, 1, 4))

m = [[1, 2], [3, 4]]
print(matrixReshape(m, 2, 4))
