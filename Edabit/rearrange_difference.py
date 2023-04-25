from audioop import reverse
from copy import copy
from posixpath import split


def rearranged_difference(number):
    number1 = str(number)
    number1 = list(number1)
    number2 = []
    for elem in str(number):
        number2.append(max(number1))
        number1.remove(max(number1))
    number3 = copy(number2)
    number3.reverse()
    return int("".join(number2)) - int("".join(number3))

def rearanged_diff(number):
    number = list(str(number))
    rev = copy(number)
    number.sort(reverse=True)
    rev.sort()

    return int("".join(number)) - int("".join(rev))

# print(rearranged_difference(1000))
print(rearanged_diff(1000))