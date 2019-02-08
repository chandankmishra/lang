# Complete the function below.


class TrieNode:
    def __init__(self):
        self.children = {}

    def leafNode(self):
        return self.children and '$' in self.children


class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.longtest = ""

    def insert(self, word):
        current_node = self.root
        for ch in word:
            if ch not in current_node.children:
                current_node.children[ch] = TrieNode()
            current_node = current_node.children[ch]
        current_node.children['$'] = TrieNode()

    def build_suffix_trie(self, word):
        n = len(word)
        for i in range(n - 1, -1, -1):
            self.insert(word[i:])

    def _helper(self, current_node, prefix):
        if not current_node:
            return 0

        dollar_count = 0
        if '$' in current_node.children:
            dollar_count += 1

        for key, node in current_node.children.items():
            count = self._helper(node, prefix + key)
            dollar_count += count

        if dollar_count > 1 and len(prefix) > len(self.longtest):
            self.longtest = prefix
        return dollar_count

    def get_longtest_repeated_substr(self):
        if not self.root:
            return 0
        self._helper(self.root, "")
        return self.longtest


def getLongestRepeatedSubstring(iString):
    obj = Trie()
    obj.build_suffix_trie(iString)
    return obj.get_longtest_repeated_substr()


print(getLongestRepeatedSubstring("abcdefghijklabcdefhiklxyz"))
