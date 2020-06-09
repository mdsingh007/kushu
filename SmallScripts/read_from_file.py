lines = open('nameslist.txt').read().split()

names = {}

for l in lines:
    if l in names:
        names[l] += 1
    else:
        names[l] = 1

#print (count)



print (names)

