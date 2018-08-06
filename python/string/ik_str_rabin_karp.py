
def rabin_karp_pattern_match(pattern, text, prime):
    d = 256
    n, m = len(text), len(pattern)
    i, j, p, t, h = 0, 0, 0, 0, 1

    for i in range(m - 1):
        h = (h * d) % prime

    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * p + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if text[i + 1] != pattern[j]:
                    break
            j += 1

            if j == m:
                print("pattern found at index", i)

            if i < n - m:
                t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % prime

                if t < 0:
                    t = t + prime


text = "chandan"
pattern = "cha"
prime = 101  # prime numberrabin_karp_pattern_match(pattern, text, prime)
