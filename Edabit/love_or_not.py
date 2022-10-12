def loves_me(petals):
    result1 = []
    number = 0
    for elem in range(petals):
        number += 1
        if number%2 == 0:
            result1.append("Loves me not")
        else:
            result1.append("Loves me")
    a = result1[-1]
    a = a.upper()
    result1.pop(-1)
    result1.append(a)
    return ", ".join(result1)


print(loves_me(113))