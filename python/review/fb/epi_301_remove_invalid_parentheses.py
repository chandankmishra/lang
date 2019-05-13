"""
301. Remove Invalid Parentheses
Remove mininum number of invalid parenthesis in order to make
the input string valid. Return all possible results
"""


class Solution:
    def __init__(self):
        self.ans = set()
        self.min_removed = float("inf")

    def helper(self, s, start, left, right, removed, prefix):
        n = len(s)
        if start == n:
            if left == right:
                if self.min_removed > removed:
                    self.ans = set()
                    self.min_removed = removed
                    self.ans.add(prefix)
                elif self.min_removed == removed:
                    self.ans.add(prefix)
        else:
            ch = s[start]
            if ch not in "()":
                self.helper(s, start + 1, left, right, removed, prefix + ch)
            else:
                self.helper(s, start + 1, left, right, removed + 1, prefix)
                if ch == "(" and left < n:
                    self.helper(s, start + 1, left + 1, right, removed, prefix + ch)
                if ch == ")" and right < left:
                    self.helper(s, start + 1, left, right + 1, removed, prefix + ch)

    def removeInvalidParentheses(self, s):
        self.helper(s, 0, 0, 0, 0, "")
        return list(self.ans)


s = Solution()
print (s.removeInvalidParentheses("()())()"))  # ["()()()", [(())()]]
