import collections
import re

class Node:
    def __init__(self, letter):
        self.letter = letter
        self.children={}
        self.positions=[]

    def leafNode(self):
        return self.children and '$' in self.children

class Trie:
    def __init__(self):
        self.root=Node('')

    def __contains__(self, word):
        current=self.root
        for letter in word:
            if letter not in current.children:
                return False
            current=current.children[letter]
        return current.leafNode()

    def __getitem__(self, word):
        current=self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter]=Node(letter)
            current=current.children[letter]
        current.children['$'] = TrieNode()
        return current.positions

def get_words(text):
    return re.sub(r'[^a-z0-9]',' ',text.lower()).split()

def create_index1(text):
    index = Trie()
    words = get_words(text)
    print (words)
    for pos, word in enumerate(words):
        index[word].append(pos)
    return index

def query_index1(index, word):
    if word in index:
        return index[word]
    else:
        return []

index = create_index1("a apple an and")
#print (index)
print (query_index1(index, "an"))
