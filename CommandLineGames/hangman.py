import random

# DONE - QQ is printing you won
# DONE - The correct letters its also showing wrong
# BUG - Displays already typed even if when it's not.


def print_letters(word, list): # KUSHAGRA, ['K', 'A']
    count = 0
    for letter in word:
        if letter in list:
            print(letter, end=' ')
        elif letter == ' ':
            print(" ", end=' ')
        else:
            print("_", end=' ')
            count += 1
    print()
    return count

# print_letters('KUSHAGRA', [1,7])
# print_letters2('KUSHAGRA', ['K', 'A'])

words = []
incorrect_letters = []
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

with open('CommandLineGames/wordslists.txt', 'r') as f:
    line = f.readline()
    while line:
        line = line.strip()
        words.append(line)
        line = f.readline()

random_word = random.choice(words)
random_word = random_word.upper()
# random_word = "LITHUANIA"
# print(random_word)

tries = 0
to_print = [random_word[0], random_word[len(random_word) - 1]]



while True:
    print_letters(random_word, to_print)
    number_of_dashes = 100
    guesed_letter = input("guess your letter: ")
    guesed_letter = guesed_letter.upper()
    # if guesed_letter in random_word and guesed_letter not in to_print:
    #     to_print.append(guesed_letter)
    #     number_of_dashes = print_letters(random_word, to_print)
    if guesed_letter in incorrect_letters and guesed_letter in letters or guesed_letter in to_print:
        print(guesed_letter, "is already used. try again")
    if guesed_letter not in incorrect_letters and guesed_letter in letters and guesed_letter not in random_word:
        print('sorry. no match')
        incorrect_letters.append(guesed_letter)
        print("incorrect_letters: ", incorrect_letters)
        tries += 1
    if guesed_letter in random_word and guesed_letter not in to_print:
        to_print.append(guesed_letter)
        number_of_dashes = print_letters(random_word, to_print) 
    elif guesed_letter not in letters:
        print("invalid entry", guesed_letter, "please only enter single alphabet")

    # if guesed_letter not in to_print:
    #     print(guesed_letter, "is already used. try again")

    if guesed_letter == "QQ":
        print(random_word)

    if tries == 5:
        print("more than 5 tries you lose")
        break    

    if number_of_dashes == 0:
        print("you win")
        break


        

        
