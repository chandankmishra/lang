class AutocompleteSystem:
    cur_sent = ""

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.map = {}
        for sentence, time in zip(sentences, times):
            self.map[sentence] = time

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """

        if c == "#":
            self.map[self.cur_sent] = self.map.get(self.cur_sent, 0) + 1
            self.cur_sent = ""
            return []

        # collect the sentences matching the input char
        results = []
        self.cur_sent += c
        for key in self.map:
            if key.startswith(self.cur_sent):
                results.append((-self.map[key], key))
        results.sort()
        res = []
        for idx in range(min(3, len(results))):
            res.append(results[idx][1])
        return res


sentences = ["i love you", "island", "ironman", "i love leetcode", "i lost book"]
times = [5, 3, 2, 2, 3]
obj = AutocompleteSystem(sentences, times)
print(obj.input('i'))
print(obj.input(' '))
print(obj.input('l'))
print(obj.input('o'))
print(obj.input('v'))
# print(obj.input(''))
