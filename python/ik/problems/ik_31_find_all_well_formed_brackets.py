def helper(left, right, nstr):
    if left == 0 and right == 0:
        print(nstr)
        return

    if left != 0:
        helper(left - 1, right, nstr + "(")

    if right > left:
        helper(left, right - 1, nstr + ")")


def find_all_well_formed_brackets(n):
    nstr = ""
    helper(n, n, nstr)


find_all_well_formed_brackets(3)

################################
############ First Approch #####
################################

# Catalen Series
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
