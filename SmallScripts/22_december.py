def list_of_multiples(num, num2):
    b =[]
    for elem in range(1,(num2 + 1)):
        b.append(num * elem)
    return b

print(list_of_multiples(5, 10))




def is_disarium(num):
    a = str(num)
    a = list(a)
    b = []
    for i, elem in enumerate(a):
        b.append(int(elem) ** (i+1))
    if sum(b) == num:
        return True
    else:
        return False

# print(is_disarium(135))

def valid(password):
    a = str(password)
    if len(a) == 4 or len(a) == 6:
        if " " not in a:
            if a.isnumeric():
                return True
    else:
        return False

print(valid(12323))