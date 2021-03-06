def is_palindrome(check):
    return check == check[::-1]


def checkPalindromePair(words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    words = {word: i for i, word in enumerate(words)}
    valid_pals = []
    for word, k in words.items():
        n = len(word)
        for j in range(n + 1):
            pref = word[:j]
            suf = word[j:]
            if is_palindrome(pref):
                back = suf[::-1]
                if back != word and back in words:
                    #print ("1", pref, suf, back)
                    valid_pals.append([words[back], k])
            if j != n and is_palindrome(suf):
                back = pref[::-1]
                if back != word and back in words:
                    #print ("2", pref, suf, back)
                    valid_pals.append([k, words[back]])
    return valid_pals


def main():
    words = ["geekf", "geeks", "or", "keeg", "abc", "bc", "aab", "cba", "baa"]
    print(checkPalindromePair(words))


main()
