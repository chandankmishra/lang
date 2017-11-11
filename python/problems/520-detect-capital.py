"""
520. Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""

import string


def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    isLower = False
    upper_cnt = 0
    for c in word:
        if string.ascii_lowercase.count(c) != 0:
            if upper_cnt > 1:
                return False
            isLower = True
        elif string.ascii_uppercase.count(c) != 0:
            upper_cnt += 1
            if isLower == True:
                return False
    return True


print(detectCapitalUse("USA"))
print(detectCapitalUse("usa"))
print(detectCapitalUse("Usa"))
print(detectCapitalUse("UsA"))
print(detectCapitalUse("USa"))
print(detectCapitalUse("uSA"))
print(detectCapitalUse("uSa"))
