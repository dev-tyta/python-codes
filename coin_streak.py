# import random
import random

chance = []
numOfStreaks = 0
for exp_num in range(1000):  # Test to be carried out 10000 times
    choice = ["H", "T"]  # The chance of having a head and a tail
    for chan in range(100):
        choi = random.choice(choice)
        chance.append(choi)

    try:
        for i in range(len(chance)):
            if chance[i] == "H":
                if chance[i + 1] == "H":
                    if chance[i + 2] == "H":
                        if chance[i + 3] == "H":
                            if chance[i + 4] == "H":
                                if chance[i + 5] == "H":
                                    numOfStreaks += 1

    except IndexError:
        numOfStreaks = 0

    try:
        for i in range(len(chance)):
            if chance[i] == "T":
                if chance[i + 1] == "T":
                    if chance[i + 2] == "T":
                        if chance[i + 3] == "T":
                            if chance[i + 4] == "T":
                                if chance[i + 5] == "T":
                                    numOfStreaks += 1

    except IndexError:
        numOfStreaks = 0

#    print(numOfStreaks)
print(f'Chance of streak: {numOfStreaks / 100}')
