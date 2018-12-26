import collections
import re

def get_words(text):
    return re.sub(r'[^a-z0-9]',' ',text.lower()).split()

def create_index1(text):
    index = collections.defaultdict(list)
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
# print (index)
print (query_index1(index, "a"))
