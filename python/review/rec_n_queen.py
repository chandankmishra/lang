# Complete the function below.
def _make_grid(cols, n):
    print (cols)
    res = []
    for j in range(n):
        nstr = ""
        for col in cols:
            nstr += "q" if j == col else "-"
        res.append(nstr)
    return res


def check_valid(col_placement, row1, col1):
    for row2 in range(row1):
        col2 = col_placement[row2]
        if col1 == col2:
            return False
        if abs(col2 - col1) == abs(row2 - row1):
            return False
    return True


def helper(result, col_placement, n, row):
    if row == n:
        # All queens are legally placed
        result.append(_make_grid(col_placement, n))
        return

    for col in range(n):
        if check_valid(col_placement, row, col):
            col_placement[row] = col
            helper(result, col_placement, n, row + 1)


def find_all_arrangements(n):
    result, col_placement = [], [0] * n
    helper(result, col_placement, n, 0)
    return result


print (find_all_arrangements(4))
