import fun_with_files

words = fun_with_files.text_in_in_file.split()

def check_if_capital(word):
    capital_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    answer = False
    for elem in word:
        if elem in capital_letters:
            answer = True
    return answer

count = 0
count2 = 0


for elem in words:
    if check_if_capital(elem) == True:
        count += 1
    if len(elem) >= 5:
        count2 += 1



            
print (check_if_capital('manish'))
print (count)
print(count2)

# check_if_capital('Manish') -> True
# check_if_capital('manish') -> False
# check_if_capital('maniSh') -> True
