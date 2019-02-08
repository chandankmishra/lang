BASE = 256


def rabin_karp(text, pattern):
    M, N = len(pattern), len(text)
    i, p_hash, t_hash = 0, 0, 0
    result = []
    power_p = BASE ** (M - 1)

    for i in range(M):
        p_hash = (BASE * p_hash + ord(pattern[i]))
        t_hash = (BASE * t_hash + ord(text[i]))

    for i in range(N - M + 1):
        if p_hash == t_hash and text[i:i + M] == pattern:
            result.append(i)
        if i + M < N:
            t_hash = BASE * (t_hash - power_p * ord(text[i]))
            t_hash = (t_hash + ord(text[i + M]))
    return result


PRIME = 10100000000000000001


def rabin_karp_prime(text, pattern):
    M, N = len(pattern), len(text)
    i, j, p_hash, t_hash = 0, 0, 0, 0
    h = 1
    result = []
    for i in range(M - 1):
        h = (h * BASE) % PRIME
    print (h)

    for i in range(M):
        p_hash = (BASE * p_hash + ord(pattern[i])) % PRIME
        t_hash = (BASE * t_hash + ord(text[i])) % PRIME

    for i in range(N - M + 1):
        if p_hash == t_hash and text[i:i + M] == pattern:
            result.append(i)

        if i < N - M:
            # t_hash = (BASE * (t_hash - ord(text[i]) * h) + ord(text[i + M])) % PRIME
            t_hash = BASE * (t_hash - ord(text[i]) * h)
            t_hash = (t_hash + ord(text[i + M])) % PRIME
            if t_hash < 0:
                t_hash = t_hash + PRIME

    return result


print(rabin_karp("abcdefabcxxybzabc", "abc"))
