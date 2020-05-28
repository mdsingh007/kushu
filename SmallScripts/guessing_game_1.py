import random

computer_choice = random.randint(1, 100)

for i in range(1000):
    my_choice = input("choose a number from 1 - 99:")
    my_choice = int(my_choice)

    if  my_choice == computer_choice:
        print("correct answer!!")
        break
    if  my_choice > computer_choice:
        print("too high!!")
    if  my_choice < computer_choice:
        print("too low!!")

print(i+1)