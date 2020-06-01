# A small script to calculate value of names
# e.g. 

# print(ord('a'))

def name_value(name):
    tot_val = 0
    for elem in name:
        tot_val += ord(elem)
    return tot_val

def reader(lines):
    names = {}
    for l in lines:
        if l in names:
            names[l] += 1
        else:
            names[l] = 1
    return names


print( name_value('Manish') )
print( name_value('Kushagra') )
print( name_value('Mridula') )

name = open('SmallScripts/names.txt')

# print(name)

txt = name.read()
list_txt = txt.split()
maximum = ''
minimum = list_txt[0]
# txt.split()
# print(txt)
# print(txt.split())

for elem in list_txt:
    print(elem, name_value(elem))
    if name_value(elem) > name_value(maximum):
        maximum = elem
    if name_value(elem) < name_value(maximum):
        maximum = elem
print(reader(list_txt))
    
print("highest number is", maximum, name_value(maximum))
print("lowest number is", minimum, name_value(minimum))


