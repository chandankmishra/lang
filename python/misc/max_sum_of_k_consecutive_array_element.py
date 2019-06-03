def get_max_sum_brute_force(lst, k):
    l = len(lst)
    max_sum = 0
    for i in range(l - k + 1):
        current_sum = 0
        for j in range(i, i + k):
            current_sum += lst[j]
    max_sum = max(max_sum, current_sum)
    return (max_sum)


def get_max_sum_sliding_window(lst, k):
    l = len(lst)
    max_sum = 0
    current_sum = 0
    for i in range(k):
        current_sum += lst[i]

    for i in range(k, l):
        current_sum += lst[i] - lst[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum


lst = [100, 200, 300, 400]
print(get_max_sum_brute_force(lst, k=2))
print(get_max_sum_sliding_window(lst, k=2))
