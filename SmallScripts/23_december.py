def combinations(num):
    a = num[0]
    for elem in num[1:]:
        a = a * elem
    return a 

print(combinations([2, 3, 4, 5]))

def arthmetic_operation(num):
    return eval(num)

print(arthmetic_operation("12 * 10"))