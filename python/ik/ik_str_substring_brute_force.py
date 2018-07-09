#
# Brute Force method for finding the substring
# Time Complexity O(n*m)
# Space Complexity O(1)
#
def substring(s, p):
    for i in range(len(s) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if s[i + j] != p[j]:
                match = False
                break
        if match:
            return i
    return -1


print(substring("aaaaaaaaaaaaaaaaaaaaaaaaab", "ab"))
