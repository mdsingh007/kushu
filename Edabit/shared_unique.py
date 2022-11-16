def letters(word1, word2):
    unique1 = []
    unique2 = []
    shared = []
    for elem in word1:
        if elem not in word2 and elem not in unique1:
            unique1.append(elem)
        elif elem in word2 and elem not in shared:
            shared.append(elem)
    for elem in word2:
        if elem not in word1 and elem not in unique2:
            unique2.append(elem)
    return "".join(sorted(shared)), "".join(sorted(unique1)), "".join(sorted(unique2))

print(letters("sharp", "soap"))
# ➞ ["aps", "hr", "o"]

print(letters("board", "bored"))
# ➞ ["bdor", "a", "e"]

print(letters("happiness", "envelope"))
# ➞ ["enp", "ahis", "lov"]

print(letters("kerfuffle", "fluffy"))
# ➞ ["flu", "ekr", "y"]
# Even with multiple matching letters (e.g. 3 f's), there should 
# only exist a single "f" in your first element.

letters("match", "ham")
# ➞ ["ahm", "ct", ""]
# "ham" does not contain any letters that are not found already 
# in "match".