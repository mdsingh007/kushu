from copy import copy
from posixpath import split


def rearranged_difference(num):
    num = str(num)
    num = list(num)
    num2 = copy(num)
    num2 = sorted(num2)

    return int("".join(num)) - int("".join(num2))

print(rearranged_difference(988722))

