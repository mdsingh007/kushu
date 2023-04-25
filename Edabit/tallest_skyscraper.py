def tallest_skyscraper(skyscrapers):
    a = len(skyscrapers)
    for index, elem in enumerate(skyscrapers):
        if 1 in skyscrapers[index]:
            return a
        a -= 1
    # elif 1 in skyscrapers[1]:
    #     return 3
    # elif 1 in skyscrapers[2]:
    #     return 2
    # elif 1 in skyscrapers[3]:
    #     return 1
    # else:
    #     return 0
         
print(tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 1]
]))
