num = input("Input an Integer: ")


def collatz(number):
    if number % 2 == 0:
        even = number // 2
        print(even)
        return even
    if number % 2 == 1 and number != 1:
        odd = 3 * number + 1
        print(odd)
        return odd
    if number == 1:
        print(1)


num = int(num)
not_one = True
while collatz(num) != 1:
    try:
        collatz(num)
    except ValueError:
        print("Input an Integer Please!!!")
