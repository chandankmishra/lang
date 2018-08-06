class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.value = 0

    def leafNode(self):
        return self and self.value != 0

    def freeNode(self):
        for c in self.children:
            if c:
                return False
        return True


class Trie:
    def __init__(self):
        self.count = 0
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _index(self, ch):
        return (ord(ch) - ord('a'))

    def insert(self, key):  # return nothing
        length = len(key)
        pnode = self.root
        self.count += 1
        for level, char in enumerate(key):
            index = self._index(char)
            if pnode.children[index] == None:
                pnode.children[index] = self.getNode()
            pnode = pnode.children[index]
        pnode.value = self.count

    def search(self, key):  # return True/False
        length = len(key)
        pnode = self.root
        for level, char in enumerate(key):
            index = self._index(char)
            if not pnode.children[index]:
                return False
            pnode = pnode.children[index]
        return pnode.leafNode()

    def _deleteHelper(self, pnode, key, level):
        length = len(key)
        if level == length:
            pnode.value = 0
            return pnode.freeNode()
        else:
            index = self._index(key[level])
            if self._deleteHelper(pnode.children[index], key, level + 1):
                del pnode.children[index]
                return (not pnode.leafNode() and pnode.freeNode())
        return False

    def deleteKey(self, key):  # return nothing
        if len(key) > 0:
            self._deleteHelper(self.root, key, 0)

    def displayTrie(self, pnode):
        print(pnode.children)
        for index in range(26):
            if not pnode.children[index]:
                continue
            self.displayTrie(pnode.children[index])


def main():
    keys = ["apple", "app", "she", "sells", "sea", "shore", "the", "by", "sheer",
            "are", "area", "base", "cat", "cater", "children", "basement",
            "a", "aaala"]
    trie = Trie()
    for key in keys:
        trie.insert(key)
    # trie.displayTrie(trie.root)
    print(trie.search("apple"))
    trie.deleteKey("apple")
    print(trie.search("apple"))
    print(trie.search("cater"))


if __name__ == '__main__':
    main()
