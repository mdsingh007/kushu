from copy import copy


def uncensor(censored, letters):
    letters = list(letters)
    # censored = list(censored)
    # censored2 = copy(censored)
    uncensored = []
    for elem in censored:
        if elem == "*":
            uncensored.append(letters.pop(0))
        else:
            uncensored.append(elem)
    return "".join(uncensored)

def uncensor2(censored, letters):
    out = []
    letters = list(letters)
    for elem in censored:
        if elem == "*":
            out.append(letters.pop(0))  
        else:
            out.append(elem)
    return "".join(out)


print(uncensor("**hello**world**", "||||||"))