def is_disarium(number):
    number2 = number
    number3 = 0
    number = str(number)
    number = list(number)
    for elem2, elem in enumerate(number):
        elem2 += 1
        number3 += int(elem)**elem2
    if number2 == number3:
        return "Yes!!!"
    else:
        return "Nope!"

print(is_disarium(135))