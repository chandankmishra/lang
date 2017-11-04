"""
Pair with given product | Set 1 (Find if any pair exists)
Given an array of distinct elements and a number x, find if there is a pair with product equal to x.

Examples :

Input : arr[] = {10, 20, 9, 40};
        int x = 400;
Output : Yes

Input : arr[] = {10, 20, 9, 40};
        int x = 190;
Output : No
"""
arr = [10, 20, 9, 40]
x = 180


def isPairExist():
    data = set()
    for i in arr:
        data.add(i)

    for i in arr:
        if x == 0 and i == 0:
            return True
        elif i == 0:
            continue
        elif x // i in data:
            return True

    return False


def returnMultPair():
    data = set()
    for i in arr:
        data.add(i)

    for i in arr:
        if x == 0 and i == 0:
            return []
        elif i == 0:
            continue
        elif x // i in data:
            return [i, x // i]
    return []


print ("Yes") if isPairExist() else print ("No")
print (returnMultPair())
