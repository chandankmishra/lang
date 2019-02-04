class TrieNode:
    def __init__(self):
        self.children = {}
        self.positions = []
        self.end_of_word = False

    def leafNode(self):
        return self.end_of_word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return [-1]
            current = current.children[letter]
        if current.leafNode():
            return current.positions
        else:
            return [-1]

    def append(self, word, index):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.end_of_word = True
        current.positions.append(index)

    def add_words(self, text):
        trie = Trie()
        i, n = 0, len(text)

        start, end = -1, -1
        for i in range(n):
            if (i == 0 or text[i - 1] == ' ') and text[i] != ' ':
                start = i
            if (i == n - 1 or text[i + 1] == ' ') and text[i] != ' ':
                end = i
            if start != -1 and end != -1:
                self.append(text[start:end + 1], start)
                start, end = -1, -1


def find_words(text, words):
    #
    # Write your code here.
    #
    result = []
    trie = Trie()
    trie.add_words(text)
    for word in words:
        ret = trie.search(word)
        result.append(ret)
    return result


def main():
    text = "my name is chandan mishra"
    words = ["my", "name", "chandan", "kumar"]
    print (find_words(text, words))


main()
