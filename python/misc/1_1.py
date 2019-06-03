class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def get_right_index(self, S, depth):
        dash = 0
        for i, ch in enumerate(S):
            if ch == '-':
                dash += 1
            else:
                if dash == depth:
                    print ("get_right_index", S, depth, i, ch)
                    return i
                dash = 0
        return len(S)

    def helper(self, S, depth):
        if len(S) == 0:
            return None

        rval = ""
        n = len(S)
        i = 0
        while i < n:
            if S[i] == '-':
                break
            rval += S[i]
            i += 1
        print ("depth", depth, "rval", rval, S)
        # print ("S", S, "rval", rval, "i", i)
        # print (S, i, rval)
        # print (S[i + depth + 1:])
        root = TreeNode(rval)
        S = S[i + depth + 1:]
        # print ("newS", S)
        index = self.get_right_index(S, depth + 1)
        print ("S", S, "depth", depth, "index", index, "left", S[:index - depth], "right", S[index:])
        # print (S, index, "right", S[index:])
        root.left = self.helper(S[:index - depth], depth + 1)
        root.right = self.helper(S[index:], depth + 1)
        return root

    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        return self.helper(S, 0)


obj = Solution()
# S = "1-2--3--4-5--6--7"
# S = "1-2--3---4-5--6---7"
S = "1-401--349---90--88"
obj.recoverFromPreorder(S)
