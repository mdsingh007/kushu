def digits_count(number):
    num_cnt = 0
    number = str(number)
    for elem in number:
        num_cnt += 1
    return num_cnt

def digit_count_recur(number):
    number = str(number)
    if not number:
        return 0
    else: 
        return 1 + digit_count_recur(number[1:])

print(digit_count_recur(123456789))