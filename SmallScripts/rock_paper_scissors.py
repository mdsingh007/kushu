import random

rock = "rock"
paper = "paper"
scissors = "scissors"

choice = ["rock", "paper", "scissors"]
computer_choice = random.choice(choice)
my_choice = input("choose: rock, paper, scissors:")

print(computer_choice)

if computer_choice == my_choice:
    print("draw")
else:
    if my_choice == rock:
        if computer_choice == paper:
            print('loose')
        else:
            print('win')

    if my_choice == paper:
        if computer_choice == scissors:
            print('loose')
        else:
            print('win')

    if my_choice == scissors:
        if computer_choice == rock:
            print('loose')
        else:
            print('win')

# if computer_choice == "rock" and my_choice == paper:
#     print ("win")

# if computer_choice == "rock" and my_choice == scissors:
#     print ("win")


# if computer_choice == "paper" and my_choice == scissors:
#     print ("win")

# if computer_choice == "rock" and my_choice == paper:
#     print ("win")

# if computer_choice == "rock" and my_choice == paper:
#     print ("win")

