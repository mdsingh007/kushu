list_a = [10, 18, 4389, 46, 309, 46346, 3239, 345, 68, 39, 25, 129]
list_b = [50, 30, 4572, 23, 347, 34638, 3637, 398, 39, 36, 28, 361]
common_number = False
for elem in list_a:
    if elem in list_b:
        common_number = True
print(common_number)
