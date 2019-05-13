#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'usernameDisparity' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY inputs as parameter.
#
class Node:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]

    def get_count(self, s):
        node = self.root
        count = 0
        for ch in s:
            if ch not in node.children:
                break
            count += 1
            node = node.children[ch]
        return count

def usernameDisparity(inputs):
    # Write your code here
    result = []
    for input_str in inputs:
        trie = Trie()
        trie.insert(input_str)
        n = len(input_str)
        count = len(input_str)
        for i in range(1,n):
            if input_str[0] != input_str[i]:
                continue
            count += trie.get_count(input_str[i:])
        result.append(count)
    return (result)

if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    inputs_count = int(input().strip())

    inputs = []

    for _ in range(inputs_count):
        inputs_item = input()
        inputs.append(inputs_item)

    result = usernameDisparity(inputs)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    '''

    inputs = ["ababaa", "ababcd", "abababab","aaaaaaaa"]
    result = usernameDisparity(inputs)
    print (result)
