def find_the_difference(list1, list2):
    difference = []
    list1 = list(list1)
    list2 = list(list2)
    if list1 == list2:
        return "There is no difference"
    for elem in list2:
        if elem not in list1:
            difference.append(elem)
        else:
            list1.remove(elem)
    if difference == [] and list1 != list2:
        return "Invalid Input"
    return ", ".join(difference)

print(find_the_difference("abcd", "abcde"))