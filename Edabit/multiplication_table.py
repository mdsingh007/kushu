def multiplication_table(number):
    number2 = []
    for elem in range(number):
        number3 = []
        elem += 1
        for elem2 in range(number):
            elem2 += 1
            number3.append(elem2*elem)
        number2.append(number3)
    return number2

print(multiplication_table(6))
# ➞ [[1]]

print(multiplication_table(3))
# ➞ [[1, 2, 3], [2, 4, 6], [3, 6, 9]]  