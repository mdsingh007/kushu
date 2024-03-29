from posixpath import split


words_to_num = [
    (1, "one"),
    (2, "two"),
    (3, "three"),
    (4, "four"),
    (5, "five"),
    (6, "six"),
    (7, "seven"),
    (8, "eight"),
    (9, "nine"),
    (10, "ten"),
    (11, "eleven"),
    (12, "twelve"),
    (13, "thirteen"),
    (14, "fourteen"),
    (15, "fifteen"),
    (16, "sixteen"),
    (17, "seventeen"),
    (18, "eighteen"),
    (19, "nineteen"),
    (20, "twenty"),
    (30, "thirty"),
    (40, "forty"),
    (50, "fifty"),
    (60, "sixty"),
    (70, "seventy"),
    (80, "eighty"),
    (90, "ninety"),
    (200, "two hundred"),
    (300, "three hundred"),
    (400, "four hundred"),
    (500, "five hundred"),
    (600, "six  hundred"),
    (700, "seven hundred"),
    (800, "eight hundred"),
    (900, "nine hundred")
]

def eng2nums(number1):
    number2 =  split(number1)
    number3 = []
    if number2[-1] == "hundred":
        number3.append("0")
        number3.append("0")

words_to_num.reverse()
n = 212
for num, numw in words_to_num:
    if num <= n:
        print(numw, end=" ")
        n = n - num