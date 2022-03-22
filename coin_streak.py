# import random

lst = [1, 1, 2, 3, 32, 2, 3, 3, 3, 3, 3, 3, 34, 5, 6, 6, 5, 4, 56, 7, 5, 4, 3, 5, 6, 7, 6]
numOfStreaks = 0
# for exp_num in range(10000):  # Test to be carried out 10000 times
#    choice = ["H", "T"]  # The chance of having a head and a tail
#    for chan in range(100):
#        chance = " "
#       choi = random.choice(choice)  # Gets a random choice between Head and Tail
#        chance += choi
for i in range(len(lst)):
    # if lst[i] == lst[i + 1] == lst[i + 2] == lst[i + 3] == lst[i + 4] == lst[i + 5] == 3:
    #    numOfStreaks += 1
    if i == i + 1 == i + 2 == i + 3 == i + 4 == i + 5:
        numOfStreaks += 1
    if len(lst) - 1 == 6:
        break
print(numOfStreaks)
