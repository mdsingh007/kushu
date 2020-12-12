def will_fit(holds, cargo):
    size = {"S" : 50, "M" : 100, "L" : 200}
    a = 0
    for index, elem in enumerate(holds):
        if cargo[index] < size[elem]:
            a += 1

    return a == len(holds)


print(will_fit(["M", "L", "L", "M"], [56, 62, 84, 90]))# ➞ True

print(will_fit(["S", "S", "S", "S", "L"], [40, 50, 60, 70 , 80, 90, 200]))# ➞ False

print(will_fit(["L", "L", "M"], [56, 62, 84, 90]))# ➞ True