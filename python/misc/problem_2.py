def helper(nset, n, i, ostr):
    if i == 1:
        ostr = '()'
    if len(ostr) == 2 * n:
        nset.add(ostr)
        return
    if len(ostr) > 2 * n:
        return
    if i == n:
        nset.add(ostr)
        return

    helper(nset, n, i + 1, ostr + ostr)
    helper(nset, n, i + 1, ostr + '()')
    helper(nset, n, i + 1, '(' + ostr + ')')
    helper(nset, n, i + 1, '()' + ostr)


def find_all_well_formed_brackets(n):
    nset = set()
    helper(nset, n, 1, "")
    print(list(nset))
    print(len(nset))


find_all_well_formed_brackets(4)
