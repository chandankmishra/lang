'''
User Accepted: 1447
User Tried: 1750
Total Accepted: 1480
Total Submissions: 4970
Difficulty: Medium
We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.

Example 1:

Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation:
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.
Note:

1 <= S.length = shifts.length <= 20000
0 <= shifts[i] <= 10 ^ 9
'''
def get_char(ch, shift):
    val = ord(ch) - ord('a')
    val = (val + shift) % 26 + ord('a')
    return chr(val)


def shiftingLetters(S, shifts):
    """
    :type S: str
    :type shifts: List[int]
    :rtype: str
    """

    l = len(shifts)
    tmp = 0
    print(S, shifts, l)
    for i in range(l - 1, -1, -1):
        tmp += shifts[i]
        shifts[i] = tmp

    ret_str = ""
    for i, ch in enumerate(S):
        ret_str += get_char(S[i], shifts[i])
    return ret_str


print(shiftingLetters("abc", [3, 5, 9]))
