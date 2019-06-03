# // Counts the number of non-unique ways to reach N.
# // Note that this algorithm counts {1,2} separately from {2,1}
# // Applies a recurrence relationship. For example, with values={1,2}:
# // cache[i] = cache[i-1] + cache[i-2]


def epp_num_of_score_permutations(scores, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(target + 1):
        for score in scores:
            if i < score:
                continue
            dp[i] += dp[i - score]
    return dp[target]

# // Counts the number of unique ways to reach N.
# // Note that this counts truly unique combinations: {1,2} is the same as {2,1}


def epi_num_of_score_combination(scores, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for score in scores:
        for j in range(score, target + 1):
            dp[j] += dp[j - score]
        print(dp)
    return dp[target]


print("num_of_score_permutation", epp_num_of_score_permutations([2, 3, 7], 12))

print("num_of_score_combination", epi_num_of_score_combination([2, 3, 7], 12))
