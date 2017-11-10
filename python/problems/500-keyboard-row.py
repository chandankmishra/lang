"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list2 = ['q', 'w', 'e', 'r', 't', 'y', 'i', 'o', 'p']
list3 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
list4 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']


def test(word):
    j = word[0].lower()
    if j in list1:
        l = 1
    elif j in list2:
        l = 2
    elif j in list3:
        l = 3
    elif j in list4:
        l = 4
    else:
        print ("invalid char", j)
        return False

    if l == 1:
        for i in word[1:]:
            if i.lower() not in list1:
                return False
    if l == 2:
        for i in word[1:]:
            if i.lower() not in list2:
                return False
    if l == 3:
        for i in word[1:]:
            if i.lower() not in list3:
                return False
    if l == 4:
        for i in word[1:]:
            if i.lower() not in list4:
                return False
    return True


def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    l = list()
    for word in words:
        if test(word):
            l.append(word)
    return l


arr = ["Hello", "Alaska", "Dad", "Peace"]

print (findWords(arr))
