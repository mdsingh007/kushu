divisers = []
user_input = input("type a number:")
user_input = int(user_input)
div = range(1, user_input)
for elem in div:
    #print (elem)
    if user_input % elem == 0:
        divisers.append(elem)
print(divisers)
