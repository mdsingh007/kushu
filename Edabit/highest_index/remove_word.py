def remove_letters(scrambled, word):
    letters = []
    letters2 = []
    for elem in scrambled:
        if elem not in letters and elem in word:
            letters.append(elem)
        else:
            letters2.append(elem)
    return letters2

remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string")
