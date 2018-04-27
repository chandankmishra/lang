class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        licensePlate = licensePlate.lower()

        words.sort(key=lambda x: (len(x)))
        nstr = ""
        for ch in licensePlate:
            if ch in string.ascii_lowercase:
                nstr += ch

        for w in words:
            flag = True
            for ch in nstr:
                if w.count(ch) < nstr.count(ch):
                    flag = False
                    break
            if flag is False:
                continue
            else:
                return w

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        lst = [0 for _ in range(26)]
        
        for c in licensePlate:
            c = c.lower()
            if c >= 'a' and c <= 'z':
                lst[ord(c) - ord('a')] += 1
        
        res = None
        
        for word in words:
            tmp = lst[:]
            for c in word.lower():
                if c >= 'a' and c <= 'z':
                    tmp[ord(c) - ord('a')] -= 1
            if max(tmp) <= 0:
                if res is None or len(word) < len(res):
                    res = word
        
        return res
                
                
