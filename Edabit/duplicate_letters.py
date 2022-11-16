def no_duplicate_letters(sentence):
    sentence = sentence.split()
    non_duplicates = []
    for elem in sentence:
        for elem2 in elem:
            if elem2 in non_duplicates:
                return False
            else:
                non_duplicates.append(elem2)
        non_duplicates = []
    return True

print(no_duplicate_letters("Fortune favours the bold."))
# ➞ True

print(no_duplicate_letters("You can lead a horse to water, but you can't make him drink."))
# ➞ True

print(no_duplicate_letters("Look before you leap."))
# ➞ False
# Duplicate letters in "Look" and "before".

print(no_duplicate_letters("An apple a day keeps the doctor away."))
# ➞ False
# Duplicate letters in "apple", "keeps", "doctor", and "away".