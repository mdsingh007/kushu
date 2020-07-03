import random

computer_choice = random.randint(1, 100)
a = computer_choice
print(computer_choice)
user = input("enter here-> ")

while True:
    if user == "h":
        computer_choice = random.randint(1, a)
    
    a = computer_choice

    if user == "l":
        computer_choice = random.randint(a, 100)

    if user == "c":
        break
    else:
        print("incorrect input")
    
    a = computer_choice


    print(a)
    user = input("enter here-> ")
