a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for elem in a:
    if elem % 2 == 0:
        print (elem)
    
even = [x for x in a if x%2 == 0]
print (even) #Hello World!!!