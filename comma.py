spam = ['apples', 'bananas', 'tofu', 'cats']


def listarg(lst):
    a = " "
    for i in range(len(lst)):
        if i < len(lst):
            a += f"{lst[i]}, "
            if i == len(lst):
                a += f"and {lst[i]}"
    print(a)


listarg(spam)
