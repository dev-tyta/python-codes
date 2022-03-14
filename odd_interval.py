total = []


def num_odd(low1, high1):
    for num in range(low1 - 1, high1 + 1):
        if num % 2 == 1:
            total.append(num)


class Solution:
    def count_odds(low: int, high: int) -> int:
        if (low % 2 == 1) and (high % 2 == 1):
            num_odd(low, high)
        elif (low % 2 == 0) and (high % 2 == 1):
            num_odd(low + 1, high)
        elif (low % 2 == 1) and (high % 2 == 0):
            num_odd(low, high - 1)
        else:
            num_odd(low + 1, high - 1)
        print(len(total))


high = int(input("Input Upper Range number:"))
low = int(input("Input Lower Range number: "))

Solution.count_odds(low, high)
