"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
"""


def checkPerfectNumber(num):
    """
    :type num: int
    :rtype: bool
    """
    if num == 1:
        return False

    sum = 1
    i = 2
    while (i * i < num):
        if num % i == 0:
            sum = sum + i + num // i
        i += 1

    if i * i == num:
        sum += i
    return True if sum == num else False


print (checkPerfectNumber(28))
