class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = []

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
    def insert(self, w, index):
        current_node = self.root
        for ch in w:
            if ch not in current_node.children:
                node = TrieNode()
                current_node.children[ch] = node
            current_node = current_node.children[ch]
            current_node.index.append(index)
        current_node.children['$'] = TrieNode()

    def build_trie(self, text):
        for i, ch in enumerate(text):
            self.insert(text[i:], i)

    # Search for the Pattern in the Trie
    def substring_search(self, pattern):
        current_node = self.root
        for ch in pattern:
            if ch not in current_node.children:
                return []
            current_node = current_node.children[ch]
        return current_node.index


# Input
text = "missiissippi"

# Build Trie
trie = Trie()
trie.build_trie(text)
print("Text is ", text)
# Search for Pattern
pattern = "iss"
print(pattern, trie.substring_search(pattern))
pattern = "ississ"
print("pattern", pattern, trie.substring_search(pattern))
pattern = "ississo"
print("pattern", pattern, trie.substring_search(pattern))
pattern = "p"
print("pattern", pattern, trie.substring_search(pattern))
pattern = "ppi"
print("pattern", pattern, trie.substring_search(pattern))
