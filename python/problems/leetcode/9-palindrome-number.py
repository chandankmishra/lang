"""
9. Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.
"""
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    new = 0
    orig = x
    while x > 0:
        new = new * 10 + x % 10
        x = x // 10
    return True if orig == new else False


print(isPalindrome(123421))
