"""
Description:

Count the number of prime numbers less than a non-negative number, n.
"""


def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 2:
        return 0

    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n)]
    p = 2
    while (p * p < n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * 2, n, p):
                prime[i] = False
        p += 1
    count = 0
    for i in prime:
        if i is True:
            count += 1
    return count - 2


num = 49
print(countPrimes(num))

# following is the inefficient solution
# def isPrime(n):
#     j = 2
#     while j * j <= n:
#         if n % j == 0:
#             return False
#         j += 1
#     return True


# def countPrimes(n):
#     """
#     :type n: int
#     :rtype: int
#     """
#     if n <= 2:
#         return 0

#     count = 0
#     for i in range(2, n):
#         if isPrime(i):
#             count += 1
#     return count
