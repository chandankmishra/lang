class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.lastChar = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for ch in word:
            if ch not in current_node.children:
                current_node.children[ch] = TrieNode()
            current_node = current_node.children[ch]
        current_node.lastChar = True

    def hasConcatWords(self, word, index, wcount):
        current_node = self.root
        n = len(word)
        for i in range(index, n):
            ch = word[i]
            if ch not in current_node.children:
                return False
            if current_node.children[ch].lastChar:
                if i == n - 1:
                    return wcount >= 1
                if self.hasConcatWords(word, i + 1, wcount + 1):
                    return True
            current_node = current_node.children[ch]
        return False


def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    trie = Trie()
    res = []
    for word in words:
        if len(word):
            trie.insert(word)

    for word in words:
        if len(word):
            if trie.hasConcatWords(word, 0, 0):
                res.append(word)
    return res


def main():
    words = ["cat", "cats", "catcats", "catsdog", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    print(findAllConcatenatedWordsInADict(words))


main()
