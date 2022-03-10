num = '*'

'''
*******
*** ***
**   **
*     *
*******

'''

cols = 9
[0, ()]

for i in range(cols+1, 0, -1):
    for j in range(i):
        print (num, end=" ")
    print()

for i in range(cols+1, 1, -1):
    for j in range(i):
        print (' ', end=" ")
    for j in range(i, cols+1):
        print ('*', end=' ')
    print()

for i in range(cols+1, 1, -1):
    for j in range(i):
        print (' ', end=" ")
    for j in range(i, cols+1):
        print ('*', end=' ')
    print()
    