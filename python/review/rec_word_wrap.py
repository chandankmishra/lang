def helper(words, limit, start):
    n = len(words)
    if start >= len(words):
        return 0

    result = float("inf")
    currentLineNonSpaceChars, noOfWordsInCurrentLine, currentLineTotalChars = 0, 0, 0
    currentLineCost = 0
    for i in range(start, n):
        # Here, current line means the first line having sequence of words [start,start+1,...,i]
        # currentLineNonSpaceChars denotes, as name suggests, sum of no of characters in current line
        # excluding spaces present between each consecutive pair of words
        currentLineNonSpaceChars += len(words[i])
        noOfWordsInCurrentLine += 1

        # currentLineTotalChars denotes, as name suggests, sum of no of characters in current line
        # including spaces present between each consecutive pair of words
        currentLineTotalChars = currentLineNonSpaceChars + noOfWordsInCurrentLine - 1
        if currentLineTotalChars > limit:
            break

        if i == n - 1:
            currentLineCost = 0
        else:
            currentLineCost = limit - currentLineTotalChars
        currentLineCost = currentLineCost * currentLineCost * currentLineCost
        result = min(result, currentLineCost + helper(words, limit, i + 1))

    return result


def solveBalancedLineBreaks(words, limit):
    return helper(words, limit, 0)


words = ["abc", "cd", "e", "ijklm"]
limit = 6
print (solveBalancedLineBreaks(words, limit))
