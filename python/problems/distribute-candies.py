"""
Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.

Example 1:
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
The sister has three different kinds of candies.
Example 2:
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1].
The sister has two different kinds of candies, the brother has only one kind of candies.
"""


def distributeCandies(candies):
    """
    :type candies: List[int]
    :rtype: int
    """
    glist = set()
    total = len(candies)
    for i in candies:
        if i not in glist:
            glist.add(i)
    max = len(glist)

    if max <= (total // 2):
        return max
    return total // 2





candies = [345,171,746,495,630,646,763,433,284,752,224,543,659,31,280,550,553,481,958,131,700,661,681,551,878,334,743,933,570,996,455,386,910,832,830,719,697,348,682,238,515,998,50,       495,44,191,238,509,564,739,99,626,730,935,662,819,240,778,722,809,932,610,205,30,353,685,181,905,267,0,79,125,26,398,104,964,766,929,132,539,673,750,756,563,642,480,237,940       ,997,44,675,765,815,428,725,252,848,155,721,94]
print(distributeCandies(candies))

candies = [1000, 1000, 2, 1, 2, 5, 3, 1]
print(distributeCandies(candies))

candies = [1000, 1, 1, 1]
print(distributeCandies(candies))

candies = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
print(distributeCandies(candies))

candies = [0, 0, 0, 4]
print(distributeCandies(candies))

candies = [1, 1, 2, 2, 3, 3]
print(distributeCandies(candies))

candies = [1, 1, 2, 3]
print(distributeCandies(candies))


    # glist = set()
    # blist = set()
    # j = 0
    # for i in candies:
    #     if j % 2 == 0:
    #         if i not in blist:
    #             blist.add(i)
    #         elif i not in glist:
    #             glist.add(i)
    #     else:
    #         if i not in glist:
    #             glist.add(i)
    #         elif i not in blist:
    #             blist.add(i)
    #     j += 1
    # print (len(blist))
    # print (len(glist))
    # return len(glist) if len(glist) > len(blist) else len(blist)

# def distributeCandies(candies):
#     """
#     :type candies: List[int]
#     :rtype: int
#     """
#     glist = set()
#     total = 0
#     for i in candies:
#         if i not in glist:
#             glist.add(i)
#         total += 1
#     max = len(glist)
#     dup = total - max


#     if max % 2 == 0 and dup % 2 == 0:
#         return dup //2 + max // 2
#     elif max % 2 == 0 and dup % 2 !=0:
#         return max % 2 + dup % 2
#     return max // 2 if max % 2 == 0 else (max // 2 + 1)
