# -  Poker Full House -------------------------------------------------------------------

def is_full_house(hand):
    if len(hand) != 5:
        return False

    else:
        hand2 = set(hand)
        hand2 = list(hand2)

        count__one = hand.count(hand2[0])
        count__two = hand.count(hand2[1])
        return len(hand2) == 2 and count__one > 1 and count__two > 1




print(is_full_house(["A", "A", "A", "K", "K"]))# ➞ True

print(is_full_house(["3", "J", "J", "3", "3"]))# ➞ True

print(is_full_house(["10", "J", "10", "10", "10"]))# ➞ False

print(is_full_house(["7", "J", "3", "4", "2"]))# ➞ False


# -  Shhh Be Quiet Function -------------------------------------------------------------------

def shhh(txt):
    if len(txt) == 0:
        return '"", whispered Edabit.'
    txt2 = str(txt)
    a = txt2[0]
    a = a.upper()
    txt2 = txt2[1:].lower()
    txt2 = list(txt2)
    txt2.insert(0, a)
    txt2.insert(0, '"')
    txt2.append('"')
    txt2 = "".join(txt2)
    return txt2 + ", whispered Edabit."



print(shhh("HI THERE!"))# ➞ '"Hi there!", whispered Edabit.'

print(shhh("tHaT'S Pretty awesOme"))# ➞ '"That's pretty awesome", whispered Edabit.'

print(shhh(""))# ➞ '"", whispered Edabit.'

'''
'hi there!, whispered Edabit' 
'"Hi there!", whispered Edabit.'


'''

# -  Shhh Be Quiet Function -------------------------------------------------------------------

def ping_pong(lst, win):
    a = []
    for elem in lst:
        a.append(elem)
        a.append('Pong!')

    if win == False:
        a = a[:-1]
    return a




print(ping_pong(["Ping!"], True))# ➞ ["Ping!", "Pong!"]

print(ping_pong(["Ping!", "Ping!"], False))# ➞ ["Ping!", "Pong!", "Ping!"]

print(ping_pong(["Ping!", "Ping!", "Ping!"], True))# ➞ ["Ping!", "Pong!", "Ping!", "Pong!", "Ping!", "Pong!"]

# -  You FAILEDPASSED the Exam -------------------------------------------------------------------


def grade_percentage(user_score, pass_score):
	s=''
	if int(user_score[:-1]) < int(pass_score[:-1]) :
		s=s+'FAILED'
	if int(user_score[:-1])>=int(pass_score[:-1]) :
		s=s+'PASSED'
	return 'You'+' '+s+' '+'the Exam'



print(grade_percentage("85%", "85%"))# ➞ "You PASSED the Exam"

print(grade_percentage("99%", "85%"))# ➞ "You PASSED the Exam"

print(grade_percentage("65%", "90%"))# ➞ "You FAILED the Exam"


# -  Curzon Numbers -------------------------------------------------------------------

def is_curzon(num):
    a = 0
    a += 1 + 2** num
    b = 1 + 2*num
    if  a % b == 0:
        return True
    else:
        return False




print(is_curzon(5))# ➞ True
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is a multiple of 11

print(is_curzon(10))# ➞ False
# 2 ** 10 + 1 = 1025
# 2 * 10 + 1 = 21
# 1025 is not a multiple of 21

print(is_curzon(14))# ➞ True
# 2 ** 14 + 1 = 16385
# 2 * 14 + 1 = 29
# 16385 is a multiple of 29