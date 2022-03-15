mus_name = []
num_mins = []
while True:
    print("Enter name of " + str(len(mus_name) + 1) + "musician and Minutes Listened or nothing to stop: ")
    name = input("Musicians Name: ")
    num = input("Minutes Listened: ")
    if name == "":
        break
    mus_name.append(name)
    num_mins.append(num)
print(f"{mus_name} and {num_mins} ")

mus_min = {}
mus_name = mus_min.keys()
num_mins = mus_min.values()
print(mus_min)
