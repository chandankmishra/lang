"""
a+b+c=0
"""


def get3sum(nums):
    n = len(nums)
    result = []
    nums.sort()  # mistake
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, n - 1
        target = -nums[i]
        while l < r:
            if nums[l] + nums[r] == target:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l, r = l + 1, r - 1  # mistake
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1

    return result


arr = [-1, 0, 1, 2, -1, -4]  # result [[-1, 0, 1],[-1, -1, 2]]
print (get3sum(arr))
