"""
394. Decode String
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""


def decodeString(s):
    stack = [["", 1]]
    num = ""
    for ch in s:
        if ch.isdigit():
            num += ch
        elif ch == "[":
            stack.append(["", int(num)])
            num = ""
        elif ch == "]":
            st, v = stack.pop()
            stack[-1][0] += st * v
        else:
            stack[-1][0] += ch
    return stack[0][0]


print (decodeString("3[a]2[bc]"))
print (decodeString("3[a2[c]]"))
print (decodeString("2[abc]3[cd]ef"))
