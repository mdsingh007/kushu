a = [5, 10, 15, 20, 25]

list_len = a.__len__() - 1
new_list = []
new_list.append(a[0])
new_list.append(a[list_len])

print(new_list)



another_list = []
another_list.append(a[0])
another_list.append(a[-1])


print(another_list)