f = open("SmallScripts/story.txt", "r")
text_in_in_file = f.read()
words_1 = text_in_in_file.lower()
words = words_1.split()

the = 0

for elem in words:
    if elem == "the":
        the += 1

print(the)

names = {}

for elem in words:
    if elem in names:
        names[elem] += 1
    else:
        names[elem] = 1
# print(names)
longest_word = ""
longest = ""
max_word = ""
max_num = 0
i = 0


for key, val in names.items():
    if i == 0:
        max_word = key
        max_num = val
        longest_word = len(key)
        longest = key
        i += 1

    if len(key) > longest_word:
        longest_word = len(key)
        longest = key
   

    if "a" or "e" or "i" or "o" or "u" in key:
        print(key, val)

    if val > max_num:
            max_word = key
            max_num = val 

if __name__ == "__main__":    
    print(f"Word which appeared max times is '{max_word}'. It appeared '{max_num}' number of times.")
    print(longest)