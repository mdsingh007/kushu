

# print(' A   B   C       D')
# print('--- --- --- --- --- ---')

a = 7

d = {}
# d[0] = 'A'
# d[1] = 'B'
# d[2] = 'C'
# d[3] = 'D'
# d[5] = 'E'
# d [4] = 'K'
# d [6] = 'Z'


b = []

word = "okapi"

word2 = len(word)

chances_remaining = 10

wrong_words = []

# for elem in range(word2):
#     d[elem] = word[elem]

for elem in range( len(word) ):
    b.append("--- ")
while True:

    if chances_remaining == 0:
        print("out of chances. GAME OVER")
        break

    if len(d) == len(word):
        print("YOU WIN!!!")
        break

    user_alpha = input("Please enter your choice alphabet: ")

    if user_alpha in word:
        d[word.find(user_alpha)] = user_alpha
    else:
        chances_remaining -= 1
        wrong_words.append(user_alpha)

    word_list = []
    for elem in range( len(word) ):
        if elem in d:
            word_list.append(" ")
            word_list.append(d[elem])
            word_list.append("  ")
        else:
            word_list.append("    ")

    print("".join(word_list))
    print("".join(b))
    print("chances remaining: ", chances_remaining)
    print("wrong words: ", wrong_words)

# print(c)
# print(b)