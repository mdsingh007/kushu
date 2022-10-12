from posixpath import split


def last_name_lensort(name_list):
    titles = [(len(x.split(' ')[-1]), x) for x in name_list]
    titles = sorted(titles)
    a = []
    for elem in titles:
        elem = list(elem)
        a.append(elem[1])
    return a


    # dict1 = {}
    # for elem in name_list:
    #     elem2 = elem.split()
    #     dict1[elem] = len(elem2[1])

    # return sorted(dict1.values())



print(last_name_lensort([
  "Jennifer Figueroa",
  "Heather Mcgee",
  "Amanda Schwartz",
  "Nicole Yoder",
  "Melissa Hoffman"
]))