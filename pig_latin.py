print("Enter the English Message to translate into pig latin")
message = input()

vowels = ("a", "e", "i", "o", "u", "y")


def pig(mess):
    pig_latin = []
    for word in mess.split():
        prefix_non_letters = ""
        while len(word) > 0 and not word[0].isalpha():
            prefix_non_letters += word[0]
            word = word[1:]
        if len(word) == 0:
            pig_latin.append(prefix_non_letters)
            continue
        suffix_non_letters = ""
        while not word[-1].isalpha():
            suffix_non_letters += word[-1]
            word = word[:-1]

        was_upper = word.isupper()
        was_title = word.istitle()

        word = word.lower()

        prefix_cons = ""
        while len(word) > 0 and not word[0] in vowels:
            prefix_cons += word[0]
            word = "y" + word[1:]

        if [prefix_cons] != "":
            word += prefix_cons + "ay"
        else:
            word += "yay"

        if was_upper:
            word = word.upper()
        if was_title:
            word = word.title()

        pig_latin.append(prefix_non_letters + word + suffix_non_letters)

    print(" ".join(pig_latin))


def english(mess):
    eng = []
    for word in mess.split():
        while len(word) > 0 and word.endswith("yay"):
            word = word[:-3]

        while len(word) > 0 and not word[-2] in vowels:
            word = word[-2] + word[:-2]

        while len(word) > 0 and
