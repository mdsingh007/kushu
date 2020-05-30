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

