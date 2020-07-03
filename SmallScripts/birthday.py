import json
from datetime import date


def dump_dictnory(dictn):
    with open("SmallScripts/birthdays.json", "w") as k:
        txt = json.dumps(dictn, indent=4, sort_keys=True, default=str)
        k.write(txt)

def read_dictnory():
    with open("SmallScripts/birthdays.json", "r") as k:
        try:
            d = json.loads(k.read())
            for k, v in d.items():
                year, month, day = v.split('-')
                year, month, day = int(year), int(month), int(day)
                d[k] = date(year, month, day)

            return d
        except json.decoder.JSONDecodeError:
            return {}


def chech_if_num(stringg):
    definition = "1234567890"
    definition = list(definition)
    integree = False
    for elem in stringg:
        if elem in definition:
            integree = True
    return integree

birth_dic = read_dictnory()

print("welcome to the birthday dictionarie. we have the names of:")
for k in birth_dic.keys():
    print(k)

while True:
    name_key = input("do you want to look up a birthday, add a birthday or check birthdays in any month. \nq for quit\na for add\nl for birthday lookup\nm for birthdays in each month\nEnter command:> ")
    
    if name_key == "q":
        break

    if name_key == "l":
        w = input("who's birthday do you want to look up? ")
        if w in birth_dic:
            print(f'Birthday of {w} is {birth_dic[w]}')
    

    if name_key == "a":
        name = input("what name? ")
        year = input("Year? ")
        month = input("month? ")
        day = input("day? ")
        if chech_if_num(year) == True and chech_if_num(month) == True and chech_if_num(day) == True:
            year = int(year)
            month = int(month)
            day = int(day)
            birthday = date(year, month, day)
            birth_dic[name] = birthday
            dump_dictnory(birth_dic)    
        else:
            print("incorrect input")

    if name_key == "m":
        month2 = input("what month? ")
    else:
        print("incorrect input")