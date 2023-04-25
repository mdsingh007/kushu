#       *
#      ***
#     *****
#    *******
#     *****
#      ***
#       *

def star(number):
    number1 = 1
    spaces = int(number) + 1
    for elem in range(number):
        spaces2 = " " * spaces
        print(spaces2, end='')
        for elem in range(number1):
            print("*", end='')
        print(spaces2, end='')
        print()
        spaces -= 1
        number1 += 2
    spaces += 2
    number1 -= 4
    for elem in range(number - 1):
        spaces2 = " " * spaces
        print(spaces2, end='')
        for elem in range(number1):
            print("*", end='')
        print(spaces2, end='')
        print()
        spaces += 1
        number1 -= 2

star(40)