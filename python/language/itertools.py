#python3 ~/lang/python/lang/itertools.py
import itertools

#itertools.count
print ("\nPrint itertools.count output (infinite) for (start=100, step=10):")
cnt = itertools.count(start=100, step=10)
for i in range(5):
    print (next(cnt), end=' ')
print ('')

#itertools.cycle
shape_list = ["square", "triangle", "circle"]
print ("\nPrint itertools.cycle output (infinite) for :", shape_list)
g = itertools.cycle(shape_list)
for i in range(5):
    print (next(g), end=' ')
print ('')

#itertools.repeat
print ("\nPrint itertools.repeat output for : (10, 3)")
cnt = itertools.repeat(10, 3)
print (list(cnt))

#itertools.combinations
my_list = [1,2,3]
print ("\nPrint itertools.combinations output for :", my_list, 3)
combinations = itertools.combinations(my_list, 3)
print (list(combinations))
combinations = itertools.combinations('ABC', 3)
print (list(combinations))

#itertools.permutations
my_list = ['a','b','c']
print ("\nPrint itertools.permutations output for :", my_list, 3)
permutations = itertools.permutations(my_list, 3)
print (list(permutations))
permutations = itertools.permutations('123', 3)
print (list(permutations))

#itertools.product
print ("\nPrint itertools.permutations output for : ('ABCD', repeat=2)")
product = itertools.product('ABC', repeat=2)
print (list(product))

#itertools.accumulate
print ("\nPrint itertools.accumulate output for : (([1,2,3,4,5]))")
res = itertools.accumulate([1,2,3,4,5])
print (list(res))

#itertools.isslice
print ("\nPrint itertools.isslice output:")
print (list(itertools.islice('ABCDEFG', 2)))
print (list(itertools.islice('ABCDEFG', 2, 4)))
print (list(itertools.islice('ABCDEFG', 2, None)))
print (list(itertools.islice('ABCDEFG', 0, None, 2)))

#itertools.groupby
def print_groupby(iterable, key=None):
    for k, g in itertools.groupby(iterable, key):
        print("'{}' : {}".format(k, list(g)))
key = lambda x: x.islower()
print ("\nPrint itertools.groupby example#1:")
print_groupby(sorted("bCAaCacAADBbB"), key)
print ("\nPrint itertools.groupby example#2:")
print_groupby(sorted("BCAACACAADBBB"))
