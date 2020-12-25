def shuffle(name):
    a = name.split()
    b = [a[1], a[0]]
    return ", ".join(b)

# print(shuffle("kushagra singh Kashvi Singh"))

def is_curzon(number_):
    a = 2 ** number_ + 1
    b = 2 * number_ + 1
    if a%b == 0:
        return True
    else:
        return False

print(is_curzon(5))


def number_len(num):
    a = str(num)
    a = list(a)
    return len(a)

print(number_len(1))