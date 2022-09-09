def majority_vote(list1):
    list2 = {}
    half = len(list1)
    half = half/2
    for elem in list1:
        if elem in list2.keys():
            list2[elem] += 1
        else:
            list2[elem] = 1
    for elem in list2.keys():
        if list2[elem] > half:
            return elem

print(majority_vote(["A", "A", "A", "B","B", "B", "C", "C", "C", "A"]))