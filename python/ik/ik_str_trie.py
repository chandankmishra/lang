class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, w):
        current_node = self.root
        for ch in w:
            if ch not in current_node.children:
                node = TrieNode()
                current_node.children[ch] = node
            current_node = current_node.children[ch]
        current_node.end_of_word = True

    def find_word(self, w):
        current_node = self.root
        for ch in w:
            if ch not in current_node.children:
                return False
            current_node = current_node.children[ch]
        return current_node.end_of_word

    def _collect_words(self, node, path, output):
        if node.end_of_word:
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


obj = Trie()
obj.add('chandan_mishra')
obj.add('chandan')
obj.add('chand')
obj.add('chan')
obj.add('veena')
obj.add('aadya')
print(obj.find_word('chandan'))
print(obj.find_word('veena1'))
print(obj.prefix_match('cha'))
