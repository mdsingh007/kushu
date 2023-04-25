from tabnanny import check
import time
import winsound
import sys

import msvcrt

def check_user_input():
    if msvcrt.kbhit():
        return msvcrt.getch() 
    
    return False

def alarm(time123):
    time.sleep(time123)
    snooze = False
    while True:
        if snooze == False:
            snooze = False
            winsound.Beep(440, 500)
            time.sleep(0.1)
            if msvcrt.kbhit():
                # print(msvcrt.getch())
                if msvcrt.getch() == b'1':
                    print("alarm stopped")
                    break
                if msvcrt.getch() == b'2':
                    snooze = True
        if snooze == True:
            print("alarm snoozed for 5 seconds")
            time.sleep(5)
            snooze = False

def play_alarm():
    for i in range(10):
        k = check_user_input()
        if k == False:
            winsound.Beep(440, 500)
            time.sleep(.2)
        else:
            return k
    return False

def alrm2(secs):
    time.sleep(secs)
    k = play_alarm()
    if k:
        if k == b'q':
            sys.exit()
        else:
            alrm2(10)            

alrm2(1)