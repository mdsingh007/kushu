import string
myList = ['I', "don’t", "like", "pickles", "in","my", "sandwiches"]

last_element = len(myList) - 1

print(myList[-3:])

myList.remove("pickles")
myList.insert(3, "tomatoes")
myList.pop()
print(myList)

alphabets = string.ascii_letters
count = 0

for word in myList:
    for alpha in word:
        if alpha in alphabets:
            count += 1

print(count)

def reverse_string(sentence):
    sentence_list = sentence.split()
    sentence_list.reverse()
    return sentence_list

print(reverse_string("hello, world"))