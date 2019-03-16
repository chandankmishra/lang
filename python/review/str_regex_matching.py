def isMatch(text, pattern):
    lt, lp = len(text), len(pattern)
    if lp == 0:
        if lt == 0:
            return True
        else:
            return False
    # if not pattern:
    #     return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        if isMatch(text, pattern[2:]):
            return True
        return first_match and isMatch(text[1:], pattern)
    else:
        return first_match and isMatch(text[1:], pattern[1:])


print (isMatch("a", "a*a"))
print (isMatch("", "a*"))
