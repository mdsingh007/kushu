# -  Mini Sudoku -------------------------------------------------------------------

def is_mini_sudoku2(sq):
    total = []
    for elem in sq:
        for i in elem:
            total.append(i)
        
        
    total.sort()
    count = 1
    if count == total[0]:
        for elem in total:
            count += 1
            if elem + 1 == count:
                pass
            else:
                return False
    else:
        return False
    
    return True



def is_mini_sudoku(sq):
    total = [x for tt in sq for x in tt]
        
    total.sort()
    out = [1,2,3,4,5,6,7,8,9]
    return total == out


print(is_mini_sudoku([[1, 3, 2], [9, 7, 8], [4, 5, 6]]))# ➞ True

print(is_mini_sudoku([[1, 1, 3], [6, 5, 4], [8, 7, 9]]))# ➞ False
# The 1 is repeated twice

print(is_mini_sudoku([[0, 1, 2], [6, 4, 5], [9, 8, 7]]))# ➞ False
# The 0 is included (outside range)

print(is_mini_sudoku([[8, 9, 2], [5, 6, 1], [3, 7, 4]]))# ➞ True