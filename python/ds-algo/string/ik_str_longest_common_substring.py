'''
Find longest common substring between two strings
'''


class TrieNode:
    def __init__(self):
        self.children = {}

    def freeNode(self):
        for ch in self.children:
            if self.children[ch]:
                return False
        return True

    def leafdollar(self):
        return self.children and '$' in self.children

    def leafpaund(self):
        return self.children and '#' in self.children


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.max_level = 0

    # Insert a word
    def insert(self, w, delim):
        current_node = self.root
        for ch in w:
            if ch not in current_node.children:
                node = TrieNode()
                current_node.children[ch] = node
            current_node = current_node.children[ch]
        current_node.children[delim] = TrieNode()

    def build_trie(self, text, delim):
        for i, ch in enumerate(text):
            self.insert(text[i:], delim)

    def _helper(self, node, level):
        if not node or not node.children:
            return 0, 0

        if node.leafdollar() and node.leafpaund():
            if level > self.max_level:
                self.max_level = level
            return 1, 1

        d, p = 0, 0
        if node.leafdollar():
            d, p = 1, 0

        if node.leafpaund():
            d, p = 0, 1

        for child in node.children:
            dollar, pound = self._helper(node.children[child], level + 1)
            # print(child, level, dollar, pound, d, p)
            d, p = d + dollar, p + pound
            if d and p:
                if level > self.max_level:
                    self.max_level = level
        return d, p

    def longest_common_substring(self):
        self._helper(self.root, 0)
        return self.max_level


# Input
text1 = "zxabcdezy"
text2 = "yzabcdezx"
# output = 6 (abcdez)

# Build Trie
trie = Trie()
trie.build_trie(text1, '$')
print("Text is ", text1)
trie.build_trie(text2, '#')
print("Text is ", text2)
# print("Longest common substring : ", end='')
print(trie.longest_common_substring())
