"""
 537. Complex Number Multiplication
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
"""


def complexNumberMultiply(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    a = a[:-1]
    b = b[:-1]
    a1, a2 = a.split("+")
    b1, b2 = b.split("+")

    f1 = int(a1) * int(b1) - int(a2) * int(b2)
    f2 = int(a1) * int(b2) + int(a2) * int(b1)

    f = str(f1) + "+" + str(f2) + "i"
    return f


num1 = "1+1i"
num2 = "1+1i"
print(complexNumberMultiply(num1, num2))
