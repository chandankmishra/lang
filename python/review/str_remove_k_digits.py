'''
402. Remove K Digits
https://leetcode.com/problems/remove-k-digits/description/
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
'''
def remove_k_digits(num, k):
    stack = []
    for d in num:
        while k and stack and stack[-1] > d:
            stack.pop()
            k -= 1
        stack.append(d)

    # if k is still positive then remove k digits from the last
    while k > 0: #corner case 112 remove 1
        stack.pop()
        k -= 1
    # above loop can be written as stack[:-k or None]
    return ''.join(stack).lstrip('0') or '0'

print (remove_k_digits("112", 1))
print (remove_k_digits("24234", 2))
print (remove_k_digits("08982002234250", 2))

