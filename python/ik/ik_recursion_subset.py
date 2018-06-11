def subset(nlst, i, s, j):
    n = len(nlst)
    if i == n:
        print(s[:j])
        return

    subset(nlst, i + 1, s, j)
    s[j] = nlst[i]
    subset(nlst, i + 1, s, j + 1)


def subset_main(nlst):
    s = [0] * len(nlst)
    subset(nlst, 0, s, 0)


nlst = [1, 2, 3, 4]
subset_main(nlst)
