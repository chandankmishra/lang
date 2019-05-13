class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls, lp = len(s), len(p)
        if ls == 0 and lp == 0:
            return True

        if lp == 0:
            return False

        first_match = ls > 0 and (s[0] == p[0] or p[0] == '.')
        if lp >= 2 and p[1] == '*':
            if self.isMatch(s, p[2:]):
                return True
            return first_match and self.isMatch(s[1:], p)    #mistake
        else:
            return first_match and self.isMatch(s[1:], p[1:])


s = Solution()
print(s.isMatch("aa", "a"))  # False
print(s.isMatch("aa", "a*"))  # True
print(s.isMatch("ab", ".*"))  # True
print(s.isMatch("aab", "c*a*b"))  # True
print(s.isMatch("mississippi", "mis*is*p*."))  # False
