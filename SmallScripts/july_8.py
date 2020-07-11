# -  The Fibonacci Number -------------------------------------------------------------------

def fibonacci(number):
    if number == 0 or number == 1:
        return 1
    elif number > 1:
        # assume 2
        return fibonacci(number - 1) + fibonacci(number - 2)

def fibonacci2(number):
    if number == 0 or number == 1:
        return 1
    elif number > 1:
        l = [1,1]
        for i in range(2, number+1):
            l.append(l[i - 1] + l[i - 2])

        return l[number]

def fibonacci3(number):
    if number == 0 or number == 1:
        return 1
    elif number > 1:
        a, b = 1, 1
        for i in range(number):
            a, b = b, a+b
        return a


print(fibonacci(3))# ➞ 3

print(fibonacci(7))# ➞ 21
print(fibonacci2(7))# ➞ 21
print(fibonacci3(7))# ➞ 21

fibonacci(12)# ➞ 233

# - easy homework -------------------------------------------------------------------

def d4(number):
    if number % 4 == 0:
        print("it is divisible by 4")
    else:
        print("it is not divisible by 4")
inp = input("enter number")

try:
    inp = int(inp)
    d4(inp)
except ValueError:
    print("Sorry. invalid input.")

# - even odd transform -------------------------------------------------------------------

def even_odd_transform(lst, num_times):
    result = lst
    for elem in range(num_times):
        for index, l in enumerate(lst):
            if l % 2 == 0:
                result[index] = result[index] - 2
            else:
                result[index] = result[index] + 2

    return result


print(even_odd_transform([3, 4, 9], 3))# ➞ [9, -2, 15]
# Since [3, 4, 9] => [5, 2, 11] => [7, 0, 13] => [9, -2, 15]

print(even_odd_transform([0, 0, 0], 10))# ➞ [-20, -20, -20]

print(even_odd_transform([1, 2, 3], 1))# ➞ [3, 0, 5]