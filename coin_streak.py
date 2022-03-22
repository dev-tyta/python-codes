import random

numOfStreaks = 0
for exp_num in range(10000):  # Test to be carried out 10000 times
    choice = ["H", "T"]  # The chance of having a head and a tail
    for chan in range(100):
        chance = " "
        choi = random.choice(choice)  # Gets a random choice between Head and Tail
        chance += choi
    for i in range(len(chance)):
        if i == i + 1 == i + 2 == i + 3 == i + 4 == i + 5 == "H":
            numOfStreaks += 1
        if i == i + 1 == i + 2 == i + 3 == i + 4 == i + 5 == "T":
            numOfStreaks += 1
print(numOfStreaks)
