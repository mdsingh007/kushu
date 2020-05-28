dic1 = {"Kushagra":10, "Manish":40}
dic2 = {"Kashvi":4, "Mridula":30, "dadu": 70}
dic3 = {"dadu":65, "dadi":60}
dic4 = {"nanu":65, "nani":60}

family = {}

mylist = [dic1, dic2, dic3, dic4]

for dic in mylist:
    for elem in dic:
        if elem in family:
            family[elem] += dic[elem]
        else:
            family[elem] = dic[elem]



# for elem in dic2:
#     family[elem] = dic2[elem]

# for elem in dic3:
#     family[elem] = dic3[elem]

# for elem in dic4:
#     family[elem] = dic4[elem]

print(family)
