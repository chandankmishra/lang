def get_max_palindrome_len(text, start, end):
    n = len(text)
    while start >= 0 and end < n and start <= end:
        if text[start] != text[end]:
            break
        start, end = start-1, end+1
    return start+1, end-start-1 

def longest_palindrome_substring(text):
    n = len(text)
    max_len, start_idx = 0, 0
    for i in range(n-1):
        start, res = get_max_palindrome_len(text, i, i+1)
        if max_len < res:
            max_len, start_idx = res, start

        start, res = get_max_palindrome_len(text, i, i)
        if max_len < res:
            max_len, start_idx = res, start
    return text[start_idx:start_idx+max_len]
 
print (longest_palindrome_substring("xabax"))
print (longest_palindrome_substring("xaax"))
print (longest_palindrome_substring("ixaaxy"))
print (longest_palindrome_substring("i2ssxxy"))
