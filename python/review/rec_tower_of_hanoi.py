def compute(n, from_peg, to_peg, use_peg, pegs, result):
    if n > 0:
        compute(n - 1, from_peg, use_peg, to_peg, pegs, result)
        pegs[to_peg].append(pegs[from_peg].pop())
        result.append([from_peg, to_peg])
        compute(n - 1, use_peg, to_peg, from_peg, pegs, result)


def tower_of_hanoi(n):
    result = []
    pegs = [[], [], []]
    for i in range(n, 0, -1):
        pegs[0].append(i)
    compute(n, 0, 1, 2, pegs, result)
    return result


print (tower_of_hanoi(4))
