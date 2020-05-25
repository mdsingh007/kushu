common_numbers = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 13, 13, 13]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for number in a:
    if number in b and number not in common_numbers:
        common_numbers.append(number)
print(common_numbers)
