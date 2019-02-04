class TrieNode:
    def __init__(self):
        self.children = {}
        self.time = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, time):
        current_node = self.root
        for ch in word:
            if ch not in current_node.children:
                current_node.children[ch] = TrieNode()
            current_node = current_node.children[ch]
        current_node.time += time

    def _traverse(self, current_node, prefix, result):
        if not current_node:
            return

        if current_node.time > 0:
            result.append((-current_node.time, prefix))

        for key, node in current_node.children.items():
            self._traverse(node, prefix + key, result)

    def lookup(self, word):
        current_node = self.root
        for ch in word:
            if ch not in current_node.children:
                return []
            current_node = current_node.children[ch]
        result = []
        self._traverse(current_node, word, result)
        return result


class AutocompleteSystem:
    cur_sent = ""

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = Trie()
        for sentence, time in zip(sentences, times):
            self.trie.insert(sentence, time)

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == "#":
            self.trie.insert(self.cur_sent, 1)
            self.cur_sent = ""
            return []

        # collect the sentences matching the input char
        results = []
        self.cur_sent += c
        results = self.trie.lookup(self.cur_sent)
        results.sort()
        res = []
        for idx in range(min(3, len(results))):
            res.append(results[idx][1])
        return res


sentences = ["i love you", "island", "ironman", "i love leetcode", "google"]
times = [5, 3, 2, 2, 1]
obj = AutocompleteSystem(sentences, times)
print(obj.input('i'))
print(obj.input(' '))
print(obj.input('l'))
print(obj.input('o'))
# print(obj.input(''))
