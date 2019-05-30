"""
How many unique, 7-digit phone numbers can a "chess knight" dial, starting from the "1"
1 2 3
4 5 6
7 8 9
  0

e.g. "1604061" and "1616161" are valid phone numbers.

For example, there are 5 unique 3-digit phone numbers that this knight can dial.
"""


# 
# Your previous Plain Text content is preserved below:
# 
# Hello Chandan.
def helper(start, move, digits, prefix, cache):
    # check the cache
    if (start, digits) in cache:
        return cache[(start, digits)]
    
    
    #base condition
    if digits == 7:
        # result[0] +=1
        cache[(start, digits)] = 1
        return 1
    
    valid_count = 0
    # recursion
    for neighbors in move[start]:
        if neighbors is None:
            continue
        
        for ch in neighbors:
            valid_count += helper(ch, move, digits+1, prefix+"ch", cache)
    cache[(start, digits)] = valid_count
    return valid_count
    

def get_unique_number_count(start):
    move = {"1":"68", "2":"79", 
             "3":"48","4":"390","5": None,
             "6":"170","7":"26","8":"13",
             "9":"24","0":"46"}

    # result = [0]
    cache = {}
    return helper(start, move, 1, start, cache)
    # return result[0]
    # digits = 7
    # return cache[(start, digits)]


print(get_unique_number_count("1"))
