import random

numOfStreaks = 0
for exp_num in range(10000):  # Test to be carried out 10000 times
    choice = ["H", "T"]  # The chance of having a head and a tail
    for chan in range(100):
        chance = " "
        choi = random.choice(choice)  # Gets a random choice between Head and Tail
        chance += choi
    print(chance)
