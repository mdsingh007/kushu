def snake_area(grid):
    grid = grid*grid
    snake = 1
    time = 0
    while True:
        if snake >= grid:
            break
        snake = snake*2
        time += 1
    return time-1

print(snake_area(24))