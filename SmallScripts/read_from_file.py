lines = open('nameslist.txt').read().split()

names = {}

#name = 'Darth'
#count = 0

for l in lines:
    if l in names:
        names[l] += 1
    else:
        names[l] = 1

#print (count)



print (names)