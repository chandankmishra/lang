def dfs(result, num, i, nsum, nstr, target, multed):
    if i == len(num):
        if nsum == target:
            result.append(nstr)
        return

    if i == 0:
        cur = int(num[i])
        dfs(result, num, i + 1, cur, str(cur), target, cur)
    else:
        cur = int(num[i])
        # if len(tsb) >= 2 and tsb[0] == "0":break
        dfs(result, num, i + 1, nsum + cur, nstr + "+" + str(cur), target, cur)
        dfs(result, num, i + 1, nsum - cur, nstr + "-" + str(cur), target, -cur)
        dfs(result, num, i + 1, nsum - multed + multed * cur, nstr + "*" + str(cur), target, multed * cur)


def generate_all_expressions(s, target):
    if s == "":
        return []
    if len(s) == 1:
        return [s]

    result = []
    dfs(result, s, 0, 0, "", target, 0)
    return result


print(generate_all_expressions("234", 6))
