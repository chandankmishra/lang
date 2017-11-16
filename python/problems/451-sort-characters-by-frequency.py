def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    sortDict = {}
    for char in s:
        if char not in sortDict:
            return 0
    return 1


print (frequencySort("tree"))
print (frequencySort("cccaaa"))
print (frequencySort("Aabb"))

mydict = {}
mydict['a'] = 2
mydict['s'] = 20
mydict['h'] = 3
# for key, value in sorted(mydict.iteritems(), key=lambda(k, v): (v, k)):
#     print "%s: %s" % (key, value)

sorted(mydict.values())
print (mydict.values())
print (mydict.keys())

s = sorted(mydict, key=mydict.__getitem__, reverse=True)
t = [value for (key, value) in sorted(mydict.items(), reverse=True)]
