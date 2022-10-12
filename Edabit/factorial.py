# 5! - 5*4*3*2*1
# 3! - 3*2*1
# 8! - 8*7*6*5!


def do_factorial(n):
    if n <= 1:
        return 1
    else:
        mul = do_factorial(n-1)*n
        return mul


print(do_factorial(2))