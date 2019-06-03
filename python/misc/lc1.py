def binaryGap(N):
    tmp, count = N, 0
    while tmp:
        tmp = tmp & (tmp - 1)
        count += 1
        if count == 2:
            break
    if count < 2:
        return 0

    start = -1
    diff = 0
    for i in range(32):
        tmp = 1 << i
        if tmp > N:
            break
        if tmp & N:
            if start != -1:
                diff = max(diff, i - start)
            start = i
        # print(N, tmp, i, start, diff)
    return (diff)


a = 12
print(binaryGap(22))
print(binaryGap(5))
print(binaryGap(6))
print(binaryGap(8))
