#code
lst = [1,-34,-20, 2,3,-2, 24,]
max_so_far = float("-inf")
max_till_now = 0
for i in lst:
    max_till_now += i
    if max_so_far < max_till_now:
        max_so_far = max_till_now
    if max_till_now < 0:
        max_till_now = 0
print (max_so_far)
