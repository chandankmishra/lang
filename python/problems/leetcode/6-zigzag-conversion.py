"""
6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

"""

n = 2
0   3   6
P   A   H   N
A P L S I I G


n = 3
0   4   8   12
Y   I   S   K       nrows - 0
A P L S I I G
Y   I   R   T       4

n = 4
0   7
A P L S I I G
Y   I   R   T       6
A P L S I I G
Y   I   R   T       6


def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    str1 = ""
    str2 = ""
    str3 = ""
    k = 0

    while k < len(s):
        if k % (numRows + 1) == 0:
            str1 += s[k]
            print (str1)
        if k % 2 == 1:
            str2 += s[k]
            print (str2)
        if k >= 2 and (k - 2) % (numRows + 1) == 0:
            str3 += s[k]
            print (str3)
        k += 1

    return str1 + str2 + str3


print (convert("PAYPALISHIRING", 3))
