class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.value = 0

    def leafNode(self): 
        return self and self.value != 0

    def freeNode(self):
        for c in self.children:
            if c: return False
        return True

class Trie:
    def __init__(self):
        self.count = 0
        self.root = self.getNode()

    def getNode(self):
        return TrieNode();

    def _index(self, ch):
        return (ord(ch) - ord('a'))

    def insert(self, key): #return nothing
        length = len(key)
        pnode = self.root
        self.count += 1
        for level in range(length):
            index = self._index(key[level])
            if pnode.children[index] == None:
                pnode.children[index] = self.getNode()
            pnode = pnode.children[index]
        pnode.value = self.count

    def search(self, key): #return True/False
        length = len(key)
        pnode = self.root
        for level in range(length):
            index = self._index(key[level])
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
            if self._deleteHelper(pnode.children[index], key, level+1):
                del pnode.children[index]
                return (not pnode.leafNode() and pnode.freeNode())
        return False

    def deleteKey(self, key): #return nothing
        if len(key) > 0: self._deleteHelper(self.root, key, 0)
    
    def displayTrie(self, pnode):
        print (pnode.children)
        for index in range(26):
            if not pnode.children[index]:
                continue
            self.displayTrie(pnode.children[index])

    '''
    Perform a LPM Search for a Key
    '''
    def lpmsearch(self, key): #return lpm matched string or empty
        length = len(key)
        pnode = self.root
        lindex = -1
        for level in range(length):
            index = self._index(key[level])
            if pnode.leafNode(): 
                lindex = level
            if not pnode.children[index]: break
            pnode = pnode.children[index]
        return "< Empty >" if lindex == -1 else key[:lindex]


    '''
    Get the common prefix among a set of strings
    '''
    def _countChildren(self, pnode):
        count = 0
        for index in range(26):
            if pnode.children[index]: 
                count += 1
                idx = index 
        return idx, count

    def getCommonPrefix(self, pnode):
        lpmidx = -1
        nstr = ""
        index = 0
        while (pnode):
            index, cnt = self._countChildren(pnode)
            if (cnt > 1): break
            if pnode.leafNode(): break
            nstr += chr(ord('a') + index)
            pnode = pnode.children[index]
            lpmidx = index
        return "<None>" if lpmidx == -1 else nstr
                
def main():
    keys = ["she", "sells", "sea", "shore", "the", "by", "sheer",
            "are", "area", "base", "cat", "cater", "children", "basement",
            "a", "aaala"]
    trie = Trie()
    for key in keys: trie.insert(key)
    #trie.displayTrie(trie.root)
    patten = "apple"
    print("{} {}".format(patten, "Present in trie" if trie.search(patten) else "Not present in trie"))
    trie.deleteKey(keys[0])
    print("{} {}".format(patten, "Present in trie" if trie.search(patten) else "Not present in trie"))
    print("{} {}".format(keys[6], "Present in trie" if trie.search(keys[6]) else "Not present in trie"))

    # perform the lpm match
    print (trie.lpmsearch("caterer"))
    print (trie.lpmsearch("child"))
    print (trie.lpmsearch("aaalappp"))


    # get the common prefix among set of string
    trie = None
    keys = ["geeksforgeeks", "geeks", "geek", "geekzer"]
    trie = Trie()
    for key in keys: trie.insert(key)
    print (trie.getCommonPrefix(trie.root))

if __name__ == '__main__':
    main()
