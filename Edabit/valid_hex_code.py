from string import ascii_lowercase


def is_valid_hex_code(sentence):
    sentence = list(sentence)
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letter = ["a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"]
    if sentence[0] == "#":
        sentence.pop(0)
        if len(sentence) == 6:
            for elem in sentence:
                if elem.isnumeric() == True:
                    elem = int(elem)
                    if elem in number:
                        pass
                    else:
                        return False
                elif elem.isalpha() == True:
                    if elem in letter:
                        pass
                    else:
                        return False
                else:
                    return False
            
        else:
            return False
    else:
        return False
    return True


print(is_valid_hex_code("#CD5C5C"))
# ➞ True

print(is_valid_hex_code("#EAECEE"))
# ➞ True

print(is_valid_hex_code("#eaecee"))
# ➞ True

print(is_valid_hex_code("#CD5C58C"))
# ➞ False
# Length exceeds 6

print(is_valid_hex_code("#CD5C5Z"))
# ➞ False
# Not all alphabetic characters in A-F

print(is_valid_hex_code("#CD5C&C"))
# ➞ False
# Contains unacceptable character

print(is_valid_hex_code("CD5C5C"))
# ➞ False
# Missing #