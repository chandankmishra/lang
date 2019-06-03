
def get_permutation(nlst, start):
    if start == len(nlst) - 1:
        if nlst[-1] in ['0', '1', '3', '5', '7', '9']:
            return False
        print(nlst)
        # print(''.join(nlst))
        if nlst[0] == '0':
            return False
        nstr = ''.join(nlst)
        n = int(nstr)
        # print(nlst, nstr, n, n & n - 1)
        return not (n & n - 1)

    for i in range(start, len(nlst)):
        nlst[start], nlst[i] = nlst[i], nlst[start]
        if get_permutation(nlst, start + 1) is True:
            return True
        nlst[start], nlst[i] = nlst[i], nlst[start]
    return False


def reorderedPowerOf2(N):
    if N & N - 1 == 0:
        return True

    nstr = str(N)
    nlst = list(nstr)
    # for i in range(len(nstr)):
    return get_permutation(nlst, 0)


# print(reorderedPowerOf2(1))
# print(reorderedPowerOf2(10))
# print(reorderedPowerOf2(16))
# print(reorderedPowerOf2(24))
print(reorderedPowerOf2(368407186))
