import random


def print_letters(word, list): # KUSHAGRA, ['K', 'A']
    for letter in word:
        if letter in list:
            print(letter, end=' ')
        else:
            print("_", end=' ')
    print()

# print_letters('KUSHAGRA', [1,7])
# print_letters2('KUSHAGRA', ['K', 'A'])

words = []

with open('CommandLineGames/wordslists.txt', 'r') as f:
    line = f.readline()
    while line:
        line = line.strip()
        words.append(line)
        line = f.readline()

random_word = random.choice(words)
print(random_word)


to_print = [random_word[0], random_word[len(random_word) - 1]]

print_letters(random_word, to_print)
guesed_letter = input("guess your letter")


while True:
    if guesed_letter in random_word:
        to_print.append(guesed_letter)
        print_letters(random_word, to_print)
    else:
        print('incorrect')
    guesed_letter = input("guess your letter")


        

        
