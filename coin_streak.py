import random

numOfStreaks = 0
for exp_num in range(10000):  # Test to be carried out 10000 times
    choice = ["H", "T"]  # The chance of having a head and a tail
    for chan in range(100):
        chance = []
        chance = chance.append(random.choice(choice))
