def is_num_prime(num, ndict):
    if num in ndict:
        return ndict[num]

    if num < 2:
        ndict[num] = False
    else:
        ndict[num] = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                ndict[num] = False
                break
            i += 1
    return ndict[num]


def get_prime_in_array(A):
    ndict = {}
    result = []
    for num in A:
        if is_num_prime(num, ndict):
            result.append(num)
    return result


print (get_prime_in_array([20, 13, 4, 22, 425, 224, 31, 344, 6]))


def get_prime(n):
    primes = []
    is_prime = [False, False] + [True] * (n - 1)

    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p, n + 1, p):
                is_prime[i] = False
    return primes


print(get_prime(70))
