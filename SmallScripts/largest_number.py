a = [10, 28, 2, 29, 67, 5, 8, 73839, 8278, 87238, 4]
lowest_num = a[0]
for elem in a:
    if elem < lowest_num:
        lowest_num = elem
print(lowest_num)