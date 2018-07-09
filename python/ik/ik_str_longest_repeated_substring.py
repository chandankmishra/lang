'''
Find longest repeating substring in a given string
'''
class TrieNode:
    def __init__(self):
        self.children = {}

    def freeNode(self):
        for ch in self.children:
            if self.children[ch]:
                return False
        return True

    def leafNode(self):
        return self.children and '$' in self.children


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.max_level = 0

    # Insert a word
    def insert(self, w):
        current_node = self.root
        for ch in w:
            if ch not in current_node.children:
                node = TrieNode()
                current_node.children[ch] = node
            current_node = current_node.children[ch]
        current_node.children['$'] = TrieNode()

    def build_trie(self, text):
        for i, ch in enumerate(text):
            self.insert(text[i:])

    def _helper(self, node, level):
        if not node or not node.children:
            return 0
        if node.leafNode():
            return 1

        dollar_cnt = 0
        for child in node.children:
            dollar_cnt += self._helper(node.children[child], level + 1)

        if dollar_cnt >= 2:
            if level > self.max_level:
                self.max_level = level
        return dollar_cnt

    # Search for the Pattern in the Trie
    def longest_repeated_substring(self):
        self._helper(self.root, 0)
        return self.max_level


# Input
text = "missiissippi"  # ans should be 4 (issi) but 3 is coming !!
# text = "aaaaacaaaaad" # ans should be 5 (aaaaa)


# Build Trie
trie = Trie()
trie.build_trie(text)
print("Text is ", text)

# Find longest repeating substring
print(trie.longest_repeated_substring())
