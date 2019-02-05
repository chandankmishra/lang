def remove_k_digits(num, k):
    out = []
    for d in num:
        while k and out and out[-1] > d:
            out.pop()
            k -= 1
        out.append(d)
    out = out[:-k or None]
    outstr = ''.join(out).lstrip('0') or '0'
    return outstr

print (remove_k_digits("24234", 2))
print (remove_k_digits("08982002234250", 2))

