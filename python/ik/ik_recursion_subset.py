################################################################
# Problem Given array of character print all subset of the array.
################################################################
# First Approch by using output array and an index

# Time Complexity is 2^n * n (n to print the content)
# Space Complexity is O(n) height of the tree!


def subset_with_array(nlst, i, op, j):
    n = len(nlst)
    if i == n:  # i == n because i ==n is invalid value. for i = n-1 we still have empty (valid) subset
        print(s[:j])  # or s[0:j] -> mean 0 to j-1 element
        return
    # Generate and print all subsets of ai...an-1 & as you print each prepend output [0...j-1] to it.
    subset_with_array(nlst, i + 1, op, j)
    op[j] = nlst[i]
    subset_with_array(nlst, i + 1, op, j + 1)


def subset_with_array_main(nlst):
    op = [0] * len(nlst)
    subset_with_array(nlst, 0, op, 0)


nlst = [1, 2, 3, 4]
# subset_with_array_main(nlst)

# Same problem but by using stack instead of output array and index


def subset_with_stack(nlst, i, op):
    n = len(nlst)
    if i == n:  # i == n because i ==n is invalid value. for i = n-1 we still have empty (valid) subset
        print(op)
        return

    subset_with_stack(nlst, i + 1, op)
    op.append(nlst[i])
    subset_with_stack(nlst, i + 1, op)
    op.pop()


def subset_with_stack_main(nlst):
    op = []
    subset_with_stack(nlst, 0, op)


nlst = [1, 2, 3, 4]
# subset_with_stack_main(nlst)

################################################################
# Problem: Given an array of positive integers, print only
#          those subsets that have sum greater than nsum.
################################################################


def subset_with_sum(nlst, i, op, nsum):
    n = len(nlst)
    if i == n:   # i == n because i ==n is invalid value. for i = n-1 we still have empty (valid) subset
        if sum(op) >= nsum:
            print(op)
        return

    subset_with_sum(nlst, i + 1, op, nsum)
    op.append(nlst[i])
    subset_with_sum(nlst, i + 1, op, nsum)
    op.pop()


def subset_with_sum_main(nlst):
    op = []
    subset_with_sum(nlst, 0, op, nsum=6)


nlst = [1, 2, 3, 4]
subset_with_sum_main(nlst)
