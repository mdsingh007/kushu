def blocks(number):
    number2 = 7
    number3 = 5
    if number == 1:
        return 5
    elif number == 0:
        return 0
    else:
        for elem in range(number-1):
            number3 += number2
            number2 += 1
    return number3

print(blocks(1))
# ➞ 5

print(blocks(5))
# ➞ 39

print(blocks(2))
# ➞ 12