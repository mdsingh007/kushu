alphabet = "abcdefghijklmnopqrstuvwxyc"
def hangman(word, letters):
    word2 = []
    for elem in word:
        if elem in letters or elem not in alphabet:
            word2.append(elem)
        else:
            word2.append("-")
    return "".join(word2)

#print(hangman("heli", ["o", "s"]))

def test_hangman():
    assert hangman("heli", ["o","s"]), "- ---"
