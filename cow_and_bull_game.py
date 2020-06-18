import random


def cow_and_bulls(pnum, cnum):
    cows = 0
    bulls = 0

    pnum_list = [int(d) for d in str(pnum)]
    cnum_list = [int(d) for d in str(cnum)]

    for index, elem in enumerate(pnum_list):
        if cnum_list[index] == pnum_list[index]:
            bulls += 1
        elif cnum_list[index] in pnum_list:
            cows += 1

  
    return (cows, bulls)


random_number = random.randint(1000, 10000)
print(random_number)




while True:
    user_input = input("choose a four digit number")
    user_input = int(user_input)

    if user_input == random_number:
        print("yay")
        break
    else: 
        print("sorry")
    cow, bull = cow_and_bulls(random_number, user_input)
    print("cows:", cow, "bulls:", bull)

        
