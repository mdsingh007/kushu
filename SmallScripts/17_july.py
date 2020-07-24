# -  Shuffle the Name -------------------------------------------------------------------

def name_shuffle(txt):
    txt2 = txt.split()
    txt2.reverse()
    return " ".join(txt2)



print(name_shuffle("Donald Trump"))# ➞ "Trump Donald"

print(name_shuffle("Rosie O'Donnell"))# ➞ "O'Donnell Rosie"

print(name_shuffle("Seymour Butts"))# ➞ "Butts Seymour"

# -  Hiding the Card Number -------------------------------------------------------------------

def card_hide(txt):
    txt2 = list(txt)
    for elem in range(len(txt) - 4):
        txt2[elem] = "*"
    return "".join(txt2)


print(card_hide("1234123456785678"))# ➞ "************5678"

print(card_hide("8754456321113213"))# ➞ "************3213"

print(card_hide("35123413355523"))# ➞ "**********5523"

# -  Hiding the Card Number -------------------------------------------------------------------

def is_isogram(txt):
    txt2 = txt.lower()
    a = []
    b = 0
    for elem in txt2:
        if elem not in a:
            a.append(elem)
        else:
            b += 1
    if b == 0:
        return True
    else:
        return False



print(is_isogram("Algorism"))# ➞ True

print(is_isogram("PasSword"))# ➞ False

print(is_isogram("Consecutive"))# ➞ False

# -  Hiding the Card Number -------------------------------------------------------------------

def split(txt):
    a = []
    b = []
    c = "aeiou"
    c = list(c)
    for elem in txt:
        if elem in c:
            a.append(elem)
        else:
            b.append(elem)
    ab = a + b
    return "".join(ab)



print(split("abcde"))# ➞ "aebcd"

print(split("Hello!"))# ➞ "eoHll!"

print(split("What's the time?"))#➞ "aeieWht's th tm?"

# -  Hiding the Card Number -------------------------------------------------------------------


def last(lst, num):
    if num > len(lst):
        return "invalid"
    if num == 0:
        return []

    return lst[-num:]



print(last([1, 2, 3, 4, 5], 1))# ➞ [5]

print(last([4, 3, 9, 9, 7, 6], 3))# ➞ [9, 7, 6]

print(last([1, 2, 3, 4, 5], 6))# ➞ "invalid"

print(last([1, 2, 3, 4, 5], 0))# ➞ []

# -  Hiding the Card Number -------------------------------------------------------------------

def oddeven(num_lst):
    odd = len([x for x in num_lst if x%2 != 0])
    even = len([x for x in num_lst if x%2 == 0])
    return odd > even


print(oddeven([1, 2, 3, 4, 5, 6, 7, 8, 9]))# ➞ True

print(oddeven([1]))# ➞ True

print(oddeven([13452394823795273847528572346]))# ➞ False


# -  Simon Says -------------------------------------------------------------------
print('Simon Says --------------------------------------------------------')

def simon_says(l1, l2):
    l3 = l1
    l4 = l2
    del l4[0]
    del l3[-1]
    return l3 == l4


print(simon_says([1, 2], [5, 1]))# ➞ True

print(simon_says([1, 2], [5, 5]) )#➞ False

print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))# ➞ True

print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) )#➞ False

# - Factorial of a Number  -------------------------------------------------------------------

def fact(num):
    return num * fact(num -1) if num > 1 else 1

def fact2(num):
    l = list(range(1, num))
    return l


print(fact(0))# ➞ 1

print(fact(1))# ➞ 1

print(fact(3))# ➞ 6

print(fact(6))# ➞ 720

# - Encode Morse  -------------------------------------------------------------------

def encode_morse(txt):
    char_to_dots = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
    ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
    '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }

    a = []

    for elem in txt:
        a.append(char_to_dots[elem])
    return " ".join(a)





print(encode_morse("EDABBIT CHALLENGE"))

print(encode_morse("HELP ME !"))

# - Invert Keys and Values  -------------------------------------------------------------------

def invert(d):
    a = {}
    for key, val in d.items():
        a[val] = key
    return a




print(invert({ "z": "q", "w": "f" }))
# ➞ { "q": "z", "f": "w" }

print(invert({ "a": 1, "b": 2, "c": 3 }))
# ➞ { 1: "a", 2: "b", 3: "c" }

print(invert({ "zebra": "koala", "horse": "camel" }))
# ➞ { "koala": "zebra", "camel": "horse" }


[1,2,3,67,23,54,102,34,1,5,6......]


