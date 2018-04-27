class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        newstr = []
        i, j, cnt, n, = 0, 0, 0, len(chars)
        while j < n:
            while j < n and chars[i] == chars[j]:
                cnt += 1
                j += 1
            newstr.append(chars[j - 1])
            i += 1
            #print (i, j, cnt, newstr)
            if cnt > 1:
                while cnt > 0:
                    i += 1
                    newstr.append(str(cnt % 10))
                    cnt = cnt // 10
            i += 1
            #print (i, j, cnt, newstr)

        return newstr


s = Solution()
lst = ["a", "a", "a", "d", "b", "b", "b", "c", "c", "c"]
print(s.compress(lst))
