spam = ['apples', 'bananas', 'tofu', 'cats']
span = ["Testimony", "Oladunni", "Collins "]

def listarg(lst):
    a = " "
    for i in range(0, len(lst)):
        if i + 1 < len(lst) - 1:
            a += f"{lst[i]}, "
        if i + 1 == len(lst) - 1:
            a += f"{lst[i]} "
        if i + 1 == len(lst):
            a += f"and {lst[i]}"
    print(a)


listarg(span)
