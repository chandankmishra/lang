"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
"""


def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = list()
    for i in range(1, n + 1):
        if i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        else:
            result.append(str(i))
    return result


n = 15
print(fizzBuzz(n))

t = 10
t1 = str(t)
