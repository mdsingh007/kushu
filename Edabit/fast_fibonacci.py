def fib_fast(number):
    fib_num = [0, 1, 1]
    a = number - 2
    for elem in range(a):
        new_num = fib_num[-1] + fib_num[-2]
        fib_num.append(new_num)
    return fib_num[-1]

print(fib_fast(5))
# ➞ 5
print(fib_fast(10)) 
# ➞ 55
print(fib_fast(20)) 
# ➞ 6765
print(fib_fast(50)) 
# ➞ 12586269025