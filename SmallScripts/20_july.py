

def count_uppercase(lst):
	return sum([word.isupper() for word in "".join(lst)])


def count_uppercase2(lst):
    count = 0
    for letter in "".join(lst):
        if letter.isupper():
            count += 1
    return count


print(count_uppercase(["SOLO", "hello", "Tea", "wHat"]))# ➞ 6

print(count_uppercase(["little", "lower", "down"]))# ➞ 0

print(count_uppercase(["EDAbit", "Educate", "Coding"]))# ➞ 5


# -  Friday the 13th -------------------------------------------------------------------

def which_is_larger(f, g):
    f2 = f()
    g2 = g()

    if f2 > g2:
        return "f"
    if f2 < g2:
        return "g"
    else:
        return "neither"




print(which_is_larger(lambda: 5, lambda: 10))# ➞ "g"

print(which_is_larger(lambda: 25,  lambda: 25))# ➞ "neither"

print(which_is_larger(lambda: 505050, lambda: 5050))# ➞ "f"


# -  Friday the 13th -------------------------------------------------------------------

def mineral_formation(lst):
    a = ""
    if 1 in lst[0] and 0 in lst[-1]:
        a = "stalactites"
    if 0 in lst[0] and 1 in lst[-1]:
        a = "stalagmites"
    if 1 in lst[0] and 1 in lst[-1]:
        a = "both"
    return a




print(mineral_formation([
  [0, 1, 0, 1],
  [0, 1, 0, 1],
  [0, 0, 0, 1],
  [0, 0, 0, 0]
]))# ➞ "stalactites"

print(mineral_formation([
  [0, 0, 0, 0],
  [0, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]))# ➞ "stalagmites"

print(mineral_formation([
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]))# ➞ "both"


# -  Friday the 13th -------------------------------------------------------------------

def longestWord(txt):
    txt2 = txt.split()
    big = 0
    big2 = ""
    big3 = ""
    for elem in txt2:
        if len(elem) > big:
            big = len(elem)
            big2 = elem
        elif len(elem) == big:
            big3 = elem
    if big2 == big3:
       return txt2[0]
    return big2

def longest_word(txt):
    words = txt.split()
    words.sort(key = len, reverse=True)
    return words[0]

# print(longestWord("Hello darkness my old friend Hello darkness my old friend Hello darknesss! my old friend Hello darkness my old friend Hello Darknesss! my old friend "))# ➞ "darkness"
# print(longest_word("Hello darkness my old friend Hello darkness my old friend Hello darknesss! my old friend Hello darkness my old friend Hello Darknesss! my old friend "))# ➞ "darkness"

txt= "o tw thr eightttT four fivee sixxxx sevennn eightttt"
print(longestWord(txt))# ➞ "Hello"
print(longest_word(txt))# ➞ "Hello"

# print(longestWord("Kayla's toy is plastic"))# ➞ "Kayla's"
