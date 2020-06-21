# grid = input("how many boxes")
# grid = int(grid)

# def hline(num_times):
#     for elem in range

# grid2 = 3

def draw_grid(table):
    grid = len(table)
    for elem in range(grid):
        print(" ---", end='')
    print()

    for k in range(grid):
        for l in range(grid):
            chr = ' '
            if table[k][l] == 1:
                chr = 'x' 
            if table[k][l] == 2:
                chr = 'o' 
            print(f'| {chr} ', end="")
        print("|")

        for elem in range(grid):
            print(" ---", end='')
        print()

def check_for_win(table):
    combinations = [
        (0, 1, 1, 1, 2, 1), # vertical 1
        (0, 0, 1, 0, 2, 0), # vertical 2
        (0, 2, 1, 2, 2, 2), # vertical 3
        (0, 0, 0, 1, 0, 2), # Horizontal 1
        (1, 0, 1, 1, 1, 2), # Horizontal 2
        (2, 0, 2, 1, 2, 2), # Horizontal 3
        (0, 0, 1, 1, 2, 2), # right cross
        (0, 2, 0, 1, 0, 0), # left cross
    ]

    for a, b, c, d, e, f in combinations:
        if table[a][b] == 1 and table[c][d] == 1 and table[e][f] == 1: 
            print("player 1 wins")
        if table[a][b] == 2 and table[c][d] == 2 and table[e][f] == 2: 
            print("player 2 wins")


game2 = [   [0, 0, 0],
	        [0, 0, 0],
    	    [0, 0, 0]]


draw_grid(game2)
# l = True
player = 1

while True:
    print("player", player)
    x = input("enter row number")
    y = input("enter colum number")
    x = int(x)
    y = int(y)
    if game2[x - 1][y - 1] == 1 or game2[x - 1][y - 1] == 2:
        print("you can't do that move")
    else:
        game2 [x - 1][y - 1] = player
        draw_grid(game2)

    check_for_win(game2)

    if player == 1:
        player = 2
    else:
        player = 1






#  --- --- ---
#  --- --- --- 
