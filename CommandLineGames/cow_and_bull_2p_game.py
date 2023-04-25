import random
import getpass
from collections import namedtuple

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

def input_name_number(salutation):
    print()
    print(salutation, 'Ensure no one is looking')
    p1name = input(f'{salutation}, enter your name? ')
    
    while 1:
        p1num = getpass.getpass(f'{salutation}, enter your 4 digit number: ')

        try:
            p1num = int(p1num)
            if p1num >= 1000 and p1num <= 9999:
                break
        except BaseException as e:
            print('error')

    print(f'Thanks! {salutation}')
    return p1name, p1num


# random_number = random.randint(1000, 10000)
# print(random_number)

p1name, p1num = input_name_number('player 1')
p2name, p2num = input_name_number('player 2')

Player = namedtuple('Player', ['name', 'number'])

loopnum = 0
players = (Player(p1name, p1num), Player(p2name, p2num))
log = []
log.append(["", p1name, p2name])

#           Manish                    Kushu
# 1         1234     2B 1C            2345      0B 2C


while True:
    player = players[loopnum % 2]
    otherplayer = players[(loopnum + 1) % 2]

    print()
    print (player.name, 'turn')

    user_input = input("guess your four digit number: ")
    user_input = int(user_input)

    if user_input == otherplayer.number:
        print("yay")
        break
    else: 
        print("sorry")
    cow, bull = cow_and_bulls(otherplayer.number, user_input)
    # print("cows:", cow, "bulls:", bull)
    if loopnum %2 == 0:
        log.append([str(int(loopnum/2)+1), str(user_input) + f" - {cow}C {bull}B"])
    else:
        log[-1].append(str(user_input) + f" - {cow}C {bull}B")

    for row in log:
        print( "".join(x.ljust(20) for x in row) )

    loopnum += 1

        
