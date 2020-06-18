# grid = input("how many boxes")
# grid = int(grid)

# def hline(num_times):
#     for elem in range

grid = 3
game = [[1, 2, 0],
	    [2, 1, 0],
    	[2, 1, 1]]

for elem in range(grid):
    print(" ---", end='')
print()


for k in range(grid):
    for l in range(grid):
        print('|   ', end="")
    print("|")

    for elem in range(grid):
        print(" ---", end='')
    print()




#  --- --- ---
#  --- --- --- 
