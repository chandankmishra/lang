
def get_val(nstr):
    x_cnt, num_cnt = 0, 0
    if 'x' in nstr:
        # print(nstr)
        x_cnt = int(nstr[:-1])
    else:
        num_cnt += int(nstr)
    return x_cnt, num_cnt


def get_computation(nstr):
    alst = a.split("+")
    x_cnt, num_cnt = 0, 0
    for lst in alst:
        if '-' in lst:
            count = 0
            for klst in lst.split('-'):
                x, n = get_val(klst)
                if count == 0:
                    x_cnt, num_cnt = x_cnt + x, num_cnt + n
                else:
                    x_cnt, num_cnt = x_cnt - x, num_cnt - n
                count += 1
        else:
            x, n = get_val(lst)
            x_cnt, num_cnt = x_cnt + x, num_cnt + n
        # print(lst, x_cnt, num_cnt)
    return x_cnt, num_cnt


a = "3x+2+3x-5x+6-2x+8"
x_cnt, num_cnt = get_computation(a)
print(a, x_cnt, num_cnt)
