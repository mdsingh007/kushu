def vowel_counter(word):
    vowels = list("aeiou")
    vowel_count = 0
    for elem in word:
        if elem in vowels:
            vowel_count += 1
    print(vowel_count)

vowel_counter("kushagra")