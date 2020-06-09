colors = ["yellow", "green", "blue", "red", "orange"]
numbers = [2, 9, 15, 14, 11]



length = len(colors)

print(colors)
print(numbers)

new_list = []

for index in range(length):
    string = str(numbers[index])
    full_name = colors[index]+ ' ' +string
    if numbers[index] > 10:
        print (full_name)
    new_list.append(full_name)
#print(new_list)