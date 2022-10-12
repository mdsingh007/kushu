from copy import copy


def remove_letters(scrambled, word):
    word2 = copy(list(word)) 
    useless = []
    for elem in scrambled:
        if elem in word2:
            word2.remove(elem)
        else:
            useless.append(elem)
    return useless
            


print(remove_letters(list("hellowworld"), "helloworld"))