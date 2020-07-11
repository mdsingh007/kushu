import string
# - letters shared between two words  -------------------------------------------------------------------

def shared_letters(word1, word2):
    count = 0
    for elem in word1:
        if elem in word2:
            count += 1
    return count


print(shared_letters("apple", "meaty"))# ➞ 2
# Since "ea" is shared between "apple" and "meaty".

shared_letters("fan", "forsook")# ➞ 1

shared_letters("spout", "shout")# ➞ 4

# - move and demove a sentence  -------------------------------------------------------------------
def move(sentence):
    a = string.ascii_lowercase
    b = "bcdefghijklmnopqrstuvwxyza"
    mydict = dict( zip(a, b))
    c = []
    for elem in sentence:
        if elem in mydict:
            c.append(mydict[elem])
        else:
            c.append(elem)
    return "".join(c)

def demove(sentence):
    a = string.ascii_lowercase
    b = "bcdefghijklmnopqrstuvwxyza"
    mydict = dict( zip(b, a))
    c = []
    for elem in sentence:
        if elem in mydict:
            c.append(mydict[elem])
        else:
            c.append(elem)
    return "".join(c)


txt = "my name is kushagra"
print(txt)
print(move(txt))# ➞ "ifmmp"
print(demove(move(txt)))

move("bye")# ➞ "czf"

move("welcome")# ➞ "xfmdpnf

# - Explosion Intensity  -------------------------------------------------------------------

def boom_intensity(number):
    intensity = "b"
    intensity = list(intensity)
    if number < 2:
        intensity.insert(1, "o")
        intensity.insert(1, "o")
        return "".join(intensity)
    else:
        for elem in range(1, number + 1):
            intensity.append('o')

        intensity.append('m')

        if number % 2 == 0:
            intensity.append("!")
        
        if number % 5 == 0:
            return "".join(intensity).upper()

        return "".join(intensity)


print(boom_intensity(10))# ➞ "Boooom!"
# There are 4 "o"s and 4 is divisible by 2 (exclamation mark included)

boom_intensity(1)# ➞ "boom"
# 1 is lower than 2, so we return "boom"

# - calc_bundled_temp  -------------------------------------------------------------------

def calc_bundled_temp(layers, temprature):
    # outside_temp = 20
    # body_temp = outside_temp + outside_temp/10
    out_temp = int(temprature.split('*')[0])
    for layer in range(layers):
        out_temp += out_temp / 10

    return out_temp



print(calc_bundled_temp(1, "2*C"))

# - Explosion Intensity  -------------------------------------------------------------------

def censor(sentence):
    words = sentence.split(" ")
    out_words = []
    for word in words:
        lenword = len(word)
        if lenword > 4:
            l = ''.join(['*' for x in word])
            out_words.append(l)
        else:
            out_words.append(word)
    return " ".join(out_words)


print(censor("The code is fourty"))

print(censor("Two plus three is five"))# ➞ "Two plus ***** is five"

# censor("aaaa aaaaa 1234 12345")