"""
293. Flip Game

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

For example, given s = "++++", after one move, it may become one of the following states:

[
  "--++",
  "+--+",
  "++--"
]
If there is no valid move, return an empty list [].
"""


def generatePossibleNextMoves(s):
    """
    :type s: str
    :rtype: List[str]
    """
    l = len(s)
    if l == 1:
        return []
    elif l == 2:
        if s != "++":
            return []

    count = 0
    for i in range(0, l):
        if i < l - 1 and s[i] == s[i + 1] == "+":
            count += 1

    rlist = [list(s) for i in range(0, count)]
    count = 0
    for i in range(0, l):
        if i < l - 1 and s[i] == s[i + 1] == "+":
            rlist[count][i] = "-"
            rlist[count][i + 1] = "-"
            rlist[count] = "".join(rlist[count])
            count += 1
    return (rlist)


str1 = "++"
print(generatePossibleNextMoves(str1))
