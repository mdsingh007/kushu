fileobj = open('SmallScripts/nameslist.txt')
text_in_file = fileobj.read()
words = text_in_file.split()

names = {}

for l in words:
    if l in names:
        names[l] += 1
    else:
        names[l] = 1

#print (count)



print (names)

