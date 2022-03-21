spam = ['apples', 'bananas', 'tofu', 'cats']


def listarg(spam):
    a = " "
    for i in spam:
        if i < len(spam):
            a = a + i
            if i == len(spam):
                a = a + f"and {i}"


listarg()
