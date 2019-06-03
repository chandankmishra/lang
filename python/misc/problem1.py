def get_fleed(target, position, speed):
    ndict = []
    for p, s in zip(position, speed):
        ndict.append((target - p, s))
    ndict.sort()
    # print(ndict)
    cur_time = 0
    p_time = -1
    result = 0
    for p, s in ndict:
        cur_time = p / s
        max_time = cur_time
        if p_time < cur_time:
            result += 1
        # print(p_time, cur_time, result)
        if cur_time > p_time:
            p_time = cur_time
    return result


pos = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
target = 12
print(get_fleed(target, pos, speed))

print(get_fleed(12, [10, 8], [2, 3]))

print(get_fleed(10, [0, 4, 2], [2, 1, 3]))
