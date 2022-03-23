# import random
import random

chance = []
numOfStreaks = 0
# for exp_num in range(10000):  # Test to be carried out 10000 times
choice = ["H", "T"]  # The chance of having a head and a tail
for chan in range(100):
    choi = random.choice(choice)
    chance.append(choi)

for i in range(len(chance)):
    if chance[i] == "H":
        numOfStreaks += 1
    print(numOfStreaks)
