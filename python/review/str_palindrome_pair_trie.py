class TrieNode:
    def __init__(self):
        self.children = {}
        self.id = -1
        self.pos = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, index):
        current_node = self.root
        n = len(word)
        level = n - 1
        for level in range(n - 1, -1, -1):
            ch = word[level]
            if ch not in current_node.children:
                current_node.children[ch] = TrieNode()
            if self.isPalindrome(word, 0, level):
                current_node.pos.append(index)
            current_node = current_node.children[ch]

        current_node.id = index
        current_node.pos.append(index)

    def isPalindrome(self, word, start, end):
        s = word[start:end + 1]
        return s == s[::-1]

    def search(self, word, index, result):
        current_node = self.root
        n = len(word)
        level = n - 1
        for level in range(n):
            ch = word[level]
            if current_node.id >= 0 and current_node.id != index and self.isPalindrome(word, level, n - 1):
                result.append([index, current_node.id])

            if ch not in current_node.children:
                return
            current_node = current_node.children[ch]

        for i in current_node.pos:
            if i == index:
                continue
            result.append([index, i])


def checkPalindromePair(words):
    obj = Trie()
    for idx, word in enumerate(words):
        obj.insert(word, idx)

    result = []
    for idx, word in enumerate(words):
        obj.search(word, idx, result)
    return (result)


def main():
    words = ["geekf", "geeks", "or", "keeg", "abc", "bc", "aab", "cba", "baa"]
    print(checkPalindromePair(words))


main()
