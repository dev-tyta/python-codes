print("Favourite musician calculation. ")
print(" You are to input your top 4 favourite musician and this app helps calculate who you listen to the most")
# Let's start
done = False
while not done:
    # Put in name of top four musician and minutes listened to.
    musician1 = input("First name:")
    num_minute1 = (input("Minutes Listened:"))
    musician2 = input("Second name:")
    num_minute2 = (input("Minutes Listened:"))
    musician3 = input("Third Name:")
    num_minute3 = (input("Minutes Listened:"))
    musician4 = input("Fourth Name:")
    num_minute4 = (input("Minutes Listened: "))
    if musician1 or num_minute1 and musician2 or num_minute2 and musician3 or num_minute3 and musician4 or num_minute4 \
            == " ":
        done = True     # Closes the input code
    else:
        mus_min = {musician1: num_minute1, musician2: num_minute2, musician3: num_minute3, musician4: num_minute4}
        print(mus_min)
        minutes = list(mus_min.values())
        max_minutes = max(minutes)
        print(max_minutes)
        lis = list(mus_min.keys())
        for pip in lis:
            if mus_min.pop(pip) == max_minutes:
                print(f"Your favorite musician is {pip}")


class Pizza:
    def __init__(self, toppings):
        self._pineapple_allowed = None
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter secret password: ")
            if password == "testys7777":
                self._pineapple_allowed = value
            else:
                raise ValueError("Wrong Password❗❗❗❗❗❗❗❗❗")


pizza = Pizza(["cheese", "beef"])
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)

