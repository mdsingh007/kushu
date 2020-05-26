list_a = [10, 50, 40, 10, 36, 49, 49, 19, 20, 19]
list_b = []
for elem in list_a:
    if elem not in list_b:
        list_b.append(elem)
print(list_b)


