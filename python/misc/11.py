def is_palindrome(n):
    nstr = str(n)
    l = len(nstr)
    for i in range(l // 2):
        if nstr[i] != nstr[l - 1 - i]:
            return False
    return True


def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


n = 1
i = n
while 1:
    if is_palindrome(i) is True and is_prime(i) is True:
        print(i)
        break
    i = i + 1

print(is_palindrome(n))
print(is_prime(n))
print
