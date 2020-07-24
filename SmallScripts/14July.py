# -  Alphabet Soup -------------------------------------------------------------------

def alphabet_soup(txt):
    txt_l = list(txt)
    txt_l.sort()
    return "".join(txt_l)


print(alphabet_soup("hello"))# ➞ "ehllo"

print(alphabet_soup("edabit"))# ➞ "abdeit"

print(alphabet_soup("hacker"))# ➞ "acehkr"

print(alphabet_soup("geek"))# ➞ "eegk"

print(alphabet_soup("javascript"))# ➞ "aacijprstv"


# -  Alphabet Soup -------------------------------------------------------------------

def counterpartCharCode(txt):
    if txt.isupper():
        txt_low = txt.lower()
        return ord(txt_low)
    else:
        txt_low = txt.upper()
        return ord(txt_low)


print(counterpartCharCode("A"))# ➞ 97

print(counterpartCharCode("a"))# ➞ 65


# -  remove vowels -------------------------------------------------------------------

def remove_vowels(txt):
    vowels = "aeiouAEIOU"
    txt2 = []
    for elem in txt:
        if elem not in vowels:
            txt2.append(elem)
    return "".join(txt2)



print(remove_vowels("I have never seen a thin person drinking Diet Coke."))
#➞ " hv nvr sn  thn prsn drnkng Dt Ck."

print(remove_vowels("We're gonna build a wall!"))
#➞ "W'r gnn bld  wll!"

print(remove_vowels("Happy Thanksgiving to all--even the haters and losers!"))
#➞ "Hppy Thnksgvng t ll--vn th htrs nd lsrs!"


# -  filter list -------------------------------------------------------------------

def filter_list_old(txt):
    txt2 = []
    for elem in txt:
        if type(elem) == int:
            txt2.append(elem)
    return txt2

def filter_list(txt):
    return [x for x in txt if type(x) == int]

print(filter_list([1, 2, 3, "a", "b", 4]))# ➞ [1, 2, 3, 4]

print(filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]))# ➞ [0, 1729]

print(filter_list(["Nothing", "here"]))# ➞ []


# -  filter list -------------------------------------------------------------------

def left_digit(txt):
    a = [elem for elem in txt if elem.isdigit( )][0]
    return a



print(left_digit("TrAdE2W1n95!"))# ➞ 2

print(left_digit("V3r1ta$"))# ➞ 3

print(left_digit("U//DertHe1nflu3nC3"))# ➞ 1

print(left_digit("J@v@5cR1PT"))# ➞ 5


print("# -  hamming distance -------------------------------------------------------------------")

def hamming_distance2(txt1, txt2):
    diff = 0
    for x, y in zip(txt1, txt2):
        if x != y:
            diff += 1
    return diff

def hamming_distance(txt1, txt2):
    return len([x `for x, y in zip(txt1, txt2) if x != y])



print(hamming_distance("abcde", "bcdef"))# ➞ 5

print(hamming_distance("abcde", "abcde"))# ➞ 0

print(hamming_distance("strong", "strung"))# ➞ 1