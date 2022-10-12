def no_duplicate_letters(sentence):
    a = sentence.split()
    b = []
    for elem in a:
        for elem2 in elem:
            if elem2 in b:
                return False
            else:
                b.append(elem2)
        b = []
    return True

print(no_duplicate_letters("Fortune favours the bold."))