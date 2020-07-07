# - Buggy Uppercase Counting  -------------------------------------------------------------------

def count_uppercase(lst):
	# return sum(letter.isupper() for letter in word for word in lst)
    return len([x.lower() for x in "".join(lst) if x.isupper()])




def count_uppercase2(lst):
    l = []
    for x in "".join(lst):
        if x.isupper():
            l.append(x.lower())
    print (l)
    return len(l)





print(count_uppercase(["SOLO", "hello", "Tea", "wHat"]))# ➞ 6
print(count_uppercase2(["SOLO", "hello", "Tea", "wHat"]))# ➞ 6

count_uppercase(["little", "lower", "down"])# ➞ 0

count_uppercase(["EDAbit", "Educate", "Coding"])# ➞ 5

# - emphasize the words  -------------------------------------------------------------------

def emphasise(word):
    word2 = word.split()
    k = [] 
    for elem in word2:
        k.append(elem[0].upper())
        k.append(elem[1:])
    return " ".join(k)



print(emphasise("hello world")) 

# - All Occurrences of an Element in a List  -------------------------------------------------------------------

def get_indices(lst, chr):
    indices = []
    for i, elem in enumerate(lst):
        if elem == chr:
            indices.append(i)
    return indices

print(get_indices(["a", "a", "b", "a", "b", "a"], "a")) 

# - box sequence  -------------------------------------------------------------------

def box_seq(number):
    if number == 1:
        return 3
    else:
        if number % 2 == 0:
            return box_seq(number - 1) - 1
        else:
            return box_seq(number - 1) + 3

print(box_seq(5))

# - fizz buzz test  -------------------------------------------------------------------

def fizz_buzz(number):
    result = []
    for elem in range(1, number +1):
        if elem % 3 == 0 and elem % 5 == 0:
            result.append("fizzbuzz")
        
        elif elem % 3 == 0:
            result.append("fizz")

        elif elem % 5 == 0:
            result.append("buzz")
        
        else:
            result.append(elem)
    return result

print(fizz_buzz(20))