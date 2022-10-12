from copy import copy
import os

class Kanha(object):
    def __init__(self):
        pass

    def replace(self, sentence, replace1, replace2):
        return sentence.replace(replace1, replace2)

    def str_length(self, sentence):
        return len(sentence)

    def trim(self, sentence):
        sentence = list(sentence)
        sentence2 = copy(sentence)
        sentence3 = copy(sentence)
        sentence3.reverse()
        for elem in sentence2:
            if elem == " " and sentence[0] == " ":
                sentence.pop(0)
        for elem in sentence3:
            if elem == " " and sentence[-1] == " ":
                sentence.pop(-1)
        return "".join(sentence)

    def list_slice(self, sentence, d):
        return sentence[d[0] - 1 : d[1]]




magic = Kanha()

print(magic.replace("AZErty-QWErty", "E", "e"))
# ➞ "Azerty-Qwerty"

print(magic.str_length("hello world"))
# # ➞ 11

print(magic.trim("      python is awesome      "))
# # ➞ "python is awesome"

print(magic.list_slice([1, 2, 3, 4, 5], (2, 4)))
# # ➞ [ 2, 3, 4 ]