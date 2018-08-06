#python3 ~/lang/python/lang/functools.py
import functools 

#functools.reduce (function, iterable[, initializer])
print ("functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) -> ((((1+2)+3)+4)+5)")
print (functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
print ("functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 100) -> ((((1+2)+3)+4)+5+100)")
print (functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 100))

