'''
a -> at -> art -> tart -> start

[a, boy, by, am, at, art,]
art
'''
def helper(num_set, start, max_len):
    n = len(start)
    if n == max_len:
        return n, start  # 3 , ‘art’

    max_length = n #2
    result = start  # ‘at’
    for i in range(n+1):
        for ch in "abcdefghijklmnopqrstuvwxyz":
            new_word = start[:i] + ch + start[i:]     # ‘a’ + ‘a’ => ‘aa’
            if new_word not in num_set:
                continue

            ret, ret_word = helper(num_set, new_word, max_len) # ’am’
            if ret > max_length:
                max_length = ret    # 3
                result = ret_word    # ’art’

    return max_length, result

def get_longest_word(nums):
    # build the set
    num_set = set(nums)  # [a, boy, by, am, at, art]
   
    # get single letter words
    candidates = []  # [a], max_len = 3
    max_len = 0
    for num in 	nums:
        n = len(num)
        if n == 1:
             candidates.append(num)
        max_len = max(max_len, n)
     
    if len(candidates) == 0:
        return None

    max_length = 0
    result = None
    for start in candidates:
        ret_len, ret_word = helper(num_set, start, max_len) # set, ‘a’, 3
        if ret_len > max_length:
            max_length = ret_len
            result = ret_word
              
    return result #’art’

nums = ['a', 'boy', 'by', 'am', 'at', 'art','ams','aams']
print (get_longest_word(nums))

	







