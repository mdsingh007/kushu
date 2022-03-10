
txt = open('words.txt').read()

#print(txt)
print (type(txt))

a = 0
b = 0

splittext = txt.split()

for elem in splittext:
    a = a+1
    if elem == "the" or elem == "The":
        b = b + 1

print(a)

print(b)

longestword = splittext[0]

for elem in splittext[1:]:
    if len(longestword) < len(elem):
        longestword = elem

print(longestword)

c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

c = list(c)

k = 0 

for elem in txt:
    if elem in c:
        k = k + 1

print(k)









"""
How many words?
How many times 'the' comes in the text
longest word
Total capital letters
"""