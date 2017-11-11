def shortestDistance(words, word1, word2):
    """
    :type words: List[str]
    :type word1: str
    :type word2: str
    :rtype: int
    """
    l = len(words)
    idx1 = -1
    idx2 = -1
    ans = l
    for i in range(0, l):
        if words[i] == word1:
            idx1 = i
        elif words[i] == word2:
            idx2 = i
        if idx1 != -1 and idx2 != -1:
            ans = ans if ans < abs(idx1 - idx2) else abs(idx1 - idx2)

    return ans


wl = ["a", "c", "b", "b", "a"]
w1 = "a"
w2 = "b"
print(shortestDistance(wl, w1, w2))

wl = ["a", "b", "c", "d", "d"]
w1 = "a"
w2 = "d"
print(shortestDistance(wl, w1, w2))

wl = ["practice", "makes", "perfect", "coding", "makes"]
w1 = "makes"
w2 = "coding"
print(shortestDistance(wl, w1, w2))

w1 = "coding"
w2 = "practice"
print(shortestDistance(wl, w1, w2))
