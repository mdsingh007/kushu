list_a = ["kushagra", "manish", "mridula", "kashvi"]
list_b = ["singh", "singh", "sinha", "singh"]

print(list_a)
print(list_b)

merged_list = []

length = len(list_a)

for index in range(length):
    full_name = list_a[index]+ ' ' +list_b[index]
    print (full_name)
    merged_list.append(full_name)

print (merged_list)
