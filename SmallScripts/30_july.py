def validate_email(txt):
    if "@" not in txt:
        return False
    if "." not in txt:
        return False
    if txt[0] == "@":
        return False
    if txt.rindex(".") < txt.rindex("@"):
        return False
    if txt == "":
        return False
    return True



def word_builder(ltr, pos):
    k = pos[:]

    for i, l in enumerate(pos):    
        k[i] = ltr[l]

    return "".join(k)

print(word_builder(["g", "e", "o"], [1, 0, 2]))# ➞ "ego"

print(word_builder(["e", "t", "s", "t"], [3, 0, 2, 1]))# ➞ "test"

print(word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2]))# ➞ "edabit"