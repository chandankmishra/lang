counter = ['one', 'two', 'three', 'four']
season = ['winter', 'summer', 'sping', 'fall']

# for index, word in enumerate(counter):
#     if index % 2 == 0:
#         print (index, word)
#     else:
#         print (index, word.upper())

for first, second in zip(counter, season):
    print (first, second)

# count = 0
# for s in season:
#     if count % 2 == 0:
#         print (s)
#     count = count + 1

# print (list(enumerate(season)))

# for count, s in enumerate(season):
#     if count % 2 == 0:
#         print (count, s)
#     else:
#         print (count, s.upper())
