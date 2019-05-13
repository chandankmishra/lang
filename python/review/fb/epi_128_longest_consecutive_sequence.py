def longest_consecutive_sequence(nums):
    nset = set(nums)
    max_count = 0
    for num in nset:
        if num - 1 not in nset:
            current_number = num
            count = 0
            while current_number in nset:
                current_number += 1
                count += 1
            max_count = max(max_count, count)
    return max_count


nums = [100, 4, 200, 1, 3, 2]
print (longest_consecutive_sequence(nums))
