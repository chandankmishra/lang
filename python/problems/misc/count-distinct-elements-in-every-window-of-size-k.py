
# time complexity O(n*k)


def countDistinct1(arr, k):
    n = len(arr)
    for j in range(0, n - k + 1):
        hm = {}
        dist_count = 0
        for i in range(j, j + k):
            if arr[i] not in hm:
                hm[arr[i]] = 1
                dist_count += 1
        print (dist_count, end=' ')
    print ('')


# time complexity O(n)
def countDistinct2(arr, k):
    n = len(arr)
    hm = {}
    dist_count = 0
    for i in range(0, k):
        if arr[i] not in hm:
            hm[arr[i]] = 1
            dist_count += 1
        else:
            hm[arr[i]] += 1

    print (dist_count, end=' ')

    for j in range(k, n):
        if arr[j] not in hm:
            hm[arr[j]] = 1
            dist_count += 1
        else:
            hm[arr[j]] += 1

        if hm[arr[j - k]] == 1:
            del hm[arr[j - k]]
            dist_count -= 1
        else:
            hm[arr[j - k]] -= 1
        print (dist_count, end=' ')
    print ('')


arr = [1, 2, 1, 3, 4, 2, 3]
k = 4
countDistinct1(arr, k)
countDistinct2(arr, k)
