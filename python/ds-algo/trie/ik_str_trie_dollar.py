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

    # Insert a word
    def insert(self, w):
        current_node = self.root
        for ch in w:
            if ch not in current_node.children:
                node = TrieNode()
                current_node.children[ch] = node
            current_node = current_node.children[ch]
        current_node.children['$'] = TrieNode()

    def _deleteHelper(self, current_node, w, level):
        length = len(w)
        if level == length:
            del current_node.children['$']
            return current_node.freeNode()
        else:
            for ch in current_node.children:
                if self._deleteHelper(current_node.children[ch], w, level + 1):
                    del current_node.children[ch]
                return (not current_node.leafNode() and current_node.freeNode())
        return False

    # Remove a word
    def delete(self, w):  # return nothing
        if len(w) > 0:
            self._deleteHelper(self.root, w, 0)

    ################################################################
    ######################## Applications ##########################
    ################################################################
    '''
    #1 Search for a word in Trie. Return True/False
    '''

    def search(self, w):
        current_node = self.root
        for ch in w:
            if ch not in current_node.children:
                return False
            current_node = current_node.children[ch]
        return current_node.leafNode()

    '''
    #2 Do LPM search for a word. Return the maximum length word matching the input.
    '''

    def lpm_search(self, w):
        current_node = self.root
        idx = -1
        for i, ch in enumerate(w):
            if ch not in current_node.children:
                break
            current_node = current_node.children[ch]
            if '$' in current_node.children:
                idx = i + 1
        return "none" if idx == -1 else w[:idx]

    '''
    #3 Do the prefix match and return all matching words
    # This problem is also called Auto Complete
    '''

    def _collect_words(self, node, path, output):
        if not node:
            return

        if '$' in node.children:
            output.append("".join(path))

        for parent, child in node.children.items():
            path.append(parent)
            self._collect_words(child, path, output)
            path.pop()

    def prefix_match(self, prefix):
        current_node = self.root
        for ch in prefix:
            if ch not in current_node.children:
                return []
            current_node = current_node.children[ch]

        output = []
        stack = list(prefix)
        self._collect_words(current_node, stack, output)
        return output


keys = ["apple", "she", "sells", "sea", "shore", "the", "by", "sheer",
        "are", "area", "base", "cat", "cater", "children", "basement", "apples",
        "a", "aaala"]
# Build Trie
trie = Trie()
for key in keys:
    trie.insert(key)

# Search for words
print("#1 Search for words:")
print(trie.search('app'))
print(trie.search('she'))

print("#2 Delete and verify:")
print(trie.search('apple'))
print(trie.prefix_match('a'))
trie.delete('apple')
print(trie.prefix_match('a'))
print(trie.search('apple'))

print("#3 Get Longest Prefix Search (LPM):")
print("areas =>", trie.lpm_search("areas"))
print("basements =>", trie.lpm_search("basements"))

print("#4 Get all matching words with a Prefix:")
print(trie.prefix_match('are'))
