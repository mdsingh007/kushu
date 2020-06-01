# A small script to calculate value of names
# e.g. 

# print(ord('a'))

def name_value(name):
    tot_val = 0
    for elem in name:
        tot_val += ord(elem)
    return tot_val

print( name_value('Manish') )
print( name_value('Kushagra') )
print( name_value('Mridula') )

name = open('SmallScripts/names.txt')

print(name)

txt = name.read()
maximum = ''
# txt.split()
# print(txt)
# print(txt.split())

for elem in txt.split():
    print(elem, name_value(elem))
    if name_value(elem) > name_value(maximum):
        maximum = elem
    
print("highest number is", maximum, name_value(maximum))


