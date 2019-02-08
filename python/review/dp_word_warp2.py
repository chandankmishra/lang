def solveWordWrap(words, n, limit):
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
            if (j == n - 1):
                currentLineCost = 0
            else:
                currentLineCost = limit - currentLineTotalChars
            currentLineCost = currentLineCost ** 3

            dp[i] = min(currentLineCost + dp[j + 1], dp[i])

    return dp[0]


l = ["tushar", "roy", "likes", "to", "code"]
n = len(l)
M = 10
print(solveWordWrap(l, n, M))


# def solveWordWrap(words, n, line_length):
#     num_remaning_blank = line_length - len(words[0])
#     min_messiness = ([num_remaning_blank * 2] + [float("inf") * (n - 1)])
#     for i in range(1, n):
#         num_remaning_blank = line_length - len(words[i])
#         min_messiness[i] = min_messiness[i - 1] + num_remaning_blank ** 2

#         for j in reversed(range(i)):
#             num_remaning_blank -= (len(words[j]) + 1)
#             if num_remaning_blank < 0:
#                 break
#             first_j_messiness = 0 if j - i < 0 else min_messiness[j - 1]
#             current_line_messiness = num_remaning_blank ** 2
#             min_messiness[i] = min(min_messiness[i], first_j_messiness + current_line_messiness)
#     return min_messiness[-1]


'''
INF = float("inf")
def printSolution(p, n):
    k = 0
    if p[n] == 1:
        k = 1
    else:
        k = printSolution(p, p[n] - 1) + 1
    print('Line number ', k, ': From word no. ',
          p[n], 'to ', n)
    return k


def solveWordWrap(l, n, M):
    extras = [[0 for i in range(n + 1)] for i in range(n + 1)]
    lc = [[0 for i in range(n + 1)] for i in range(n + 1)]

    c = [0 for i in range(n + 1)]
    p = [0 for i in range(n + 1)]

    for i in range(n + 1):
        extras[i][i] = M - l[i - 1]
        for j in range(i + 1, n + 1):
            extras[i][j] = (extras[i][j - 1] - l[j - 1] - 1)

    for i in range(n + 1):
        for j in range(i, n + 1):
            if extras[i][j] < 0:
                lc[i][j] = INF
            elif j == n and extras[i][j] >= 0:
                lc[i][j] = 0
            else:
                lc[i][j] = (extras[i][j] * extras[i][j])

    c[0] = 0
    for j in range(1, n + 1):
        c[j] = INF
        for i in range(1, j + 1):
            if (c[i - 1] != INF and lc[i][j] != INF and ((c[i - 1] + lc[i][j]) < c[j])):
                c[j] = c[i - 1] + lc[i][j]
                p[j] = i
    printSolution(p, n)

'''
# Driver Code
# l = [3, 2, 2, 5]
# l = ["tushar", "roy", "likes", "to", "code"]
# n = len(l)
# M = 10
# print(solveWordWrap(l, n, M))


'''
def length(wordLengths, i, j):
    return sum(wordLengths[i - 1:j]) + j - i + 1


def breakLine(text, L):
    # wl = lengths of words
    wl = [len(word) for word in text.split()]

    # n = number of words in the text
    n = len(wl)

    # total badness of a text l1 ... li
    m = dict()
    # initialization
    m[0] = 0

    # auxiliary array
    s = dict()

    # the actual algorithm
    for i in range(1, n + 1):
        sums = dict()
        k = i
        while (length(wl, k, i) <= L and k > 0):
            sums[(L - length(wl, k, i))**2 + m[k - 1]] = k
            k -= 1
        m[i] = min(sums)
        s[i] = sums[min(sums)]

    # actually do the splitting by working backwords
    line = 1
    while n > 0:
        print("line " + str(line) + ": " + str(s[n]) + "->" + str(n))
        n = s[n] - 1
        line += 1


breakLine("tushar roy likes to code", 10)
'''
