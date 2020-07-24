def convert_to_roman(num):
    mapping = {
        1   : "I",
        5   : "V",
        10  : "X",
        50  : "L",
        100 : "C",
        500 : "D",
        1000: "M",
    }

    desc = list(mapping.keys())
    desc.sort(reverse=True)
    # print (desc)

    if num <= 0:
        return ""

    for i, step in enumerate(desc):
        prev_step = desc[i+1] if len(desc) <= i else 0
        
        if num > step:
            return mapping[step] + convert_to_roman(num - step)
        elif num == step:
            return mapping[step]
        elif num == step - 1:
            return "I" + mapping[step]
        elif num == step - prev_step:
            return mapping[prev_step] + mapping[step]

    # if num >= 10:
    #     return 'X' + convert_to_roman(num - 10)
    # if num >= 5:
    #     return 'V' + convert_to_roman(num - 5)
    # elif num == 5 - 1:
    #     return "IV"

    return 'I' + convert_to_roman(num - 1)

    

# print("II", convert_to_roman(2))
# print("XXV", convert_to_roman(25)) # XXV
# print("XXXIII", convert_to_roman(33)) # XXXIII
# print("XXXIV", convert_to_roman(34)) # XXXIV
print("XCI", convert_to_roman(92)) # XXXIV