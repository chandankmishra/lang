def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    # Base case:
    #   Initialize first row and col with value r, c.
    #   No of steps to convert a string to an empty string is equal to the size of the string.
    # Formula:
    # if word[i] == word[j]:
    #   dp[i][j] = dp[i-1][j-1]
    # else:
    #   dp[i][j] = min(dp[i-1][j-1]+dp[i][j-1]+dp[i-1][j])+1

    cols, rows = len(word1), len(word2)
    dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]

    # base  case
    for c in range(cols+1):
        dp[0][c] = c
    for r in range(rows+1):
        dp[r][0] = r

    # formula
    for r in range(1, rows+1):
        for c in range(1, cols+1):
            if word1[c-1] == word2[r-1]:
                dp[r][c] = dp[r-1][c-1]
            else:
                dp[r][c] = min(dp[r-1][c-1], dp[r][c-1], dp[r-1][c]) + 1
    return dp[-1][-1]
