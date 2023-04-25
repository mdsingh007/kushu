from copy import copy


def first_before_second(sentence, vowel, vowel2):
    sentence2 = copy(sentence)
    sentence2 = list(sentence)
    a = True
    if vowel in sentence and vowel2 in sentence:
        for elem in sentence:
            if vowel in sentence2 and vowel2 in sentence2:
                if elem == vowel:
                    a = True
                    sentence2.remove(vowel)
                    if vowel in sentence2 and vowel2 in sentence2:
                        sentence2.remove(vowel2)
                if elem == vowel2:
                    a = False
                    sentence2.remove(vowel)
                    if vowel in sentence2 and vowel2 in sentence2:
                        sentence2.remove(vowel2)
            else:
                return a
    else:
        return "Invalid Input"

assert first_before_second("precarious kangaroos", "r", "c")
assert first_before_second("precarious kangaroos", "p", "o")
assert first_before_second("precarious kangaroos", "o", "o") == False
assert first_before_second("prrrcccrious kangacroos", "r", "c") == False
