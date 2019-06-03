def subset_with_stack(nlst, i, op, k):
    n = len(nlst)
    if i == n:  # i == n because i ==n is invalid value. for i = n-1 we still have empty (valid) subset
        if len(op) == k:
            print(op)
        return

    subset_with_stack(nlst, i + 1, op, k)
    op.append(nlst[i])
    subset_with_stack(nlst, i + 1, op, k)
    op.pop()


def subset_with_stack_main(nlst, k):
    op = []
    subset_with_stack(nlst, 0, op, k)


nlst = [1, 2, 3, 4]
k = 2
subset_with_stack_main(nlst, k)
