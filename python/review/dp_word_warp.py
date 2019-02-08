def solveBalancedLineBreaks(words, limit):
    n = len(words)
    dp = [0] * (n + 1)
    # dp[i] = x denotes that the total minimized cost is x if we had sequence of words
    # [i,i+1,...,n-1] and we put line breaks in a most balanced way

    currentLineNonSpaceChars, noOfWordsInCurrentLine, currentLineTotalChars = 0, 0, 0
    currentLineCost = 0
    for i in range(n - 1, -1, -1):
        # currentLineNonSpaceChars denotes, as name suggests, sum of no of characters in current line
        # excluding spaces present between each consecutive pair of words
        currentLineNonSpaceChars = 0
        noOfWordsInCurrentLine = 0
        dp[i] = float("inf")
        for j in range(i, n):
            # Here, current line means the first line having sequence of words [i,i+1,...,j]
            currentLineNonSpaceChars += len(words[j])
            noOfWordsInCurrentLine += 1

            # currentLineTotalChars denotes, as name suggests, sum of no of characters in current line
            # including spaces present between each consecutive pair of words
            currentLineTotalChars = currentLineNonSpaceChars + noOfWordsInCurrentLine - 1
            if currentLineTotalChars > limit:
                break
            if j == n - 1:
                currentLineCost = 0
            else:
                currentLineCost = limit - currentLineTotalChars
            currentLineCost = currentLineCost * currentLineCost * currentLineCost

            dp[i] = min(dp[i], currentLineCost + dp[j + 1])
    return dp[0]


words = ["abc", "cd", "e", "ijklm"]
limit = 6
print (solveBalancedLineBreaks(words, limit))
