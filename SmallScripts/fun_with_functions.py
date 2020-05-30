# Create a function which displays a message to a user and returns a integer
# 
def add_list(list_a, list_b):
    list_c = []
    for elem in list_a:
        list_c.append(elem)
    for elem in list_b:
        list_c.append(elem)
    return list_c
        

def multiply_list(list_multiplier):
    new_list = []
    for elem in list_multiplier:
        new_list.append(elem * elem)
    return new_list
        

def sum_list(my_list):
    number = 0
    for elem in my_list:
        number += elem
    return number


def input_number(msg):
    number = input(msg)
    number = int(number)
    return number

# marks = input_number("Please enter age for student")

end = add_list([1, 2], [3, 4])
print(end)

# final = multiply_list([1, 2, 3, 4, 5])
# print(final)

# l = [1,2,3,4]
# total = sum_list(l)
# print(total) # 6

# mylist = [100, 300, 500]
# list_total = sum_list(mylist)
# print(list_total)


'''

[1,2,3,4,5]
[1, 4, 9, 16, 25]

'''