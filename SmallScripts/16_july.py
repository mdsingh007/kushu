# -  Transforming Words into Binary Strings -------------------------------------------------------------------

def convert_binary(txt):
    a_m = "abcdefghijklmABCDEFGHIJKLM"
    n_z = "nopqrstuvwxyzNOPQRSTUVWXYZ"
    trans_txt = []

    for elem in txt:
        if elem in a_m:
            trans_txt.append("0")
        elif elem in n_z:
            trans_txt.append("1")
    return "".join(trans_txt)


print(convert_binary("house"))# ➞ "01110"

print(convert_binary("excLAIM"))# ➞ "0100000"

print(convert_binary("moon"))# ➞ "0111"

print("# -  Transforming Words into Binary Strings -------------------------------------------------------------------")

def sum_numbers(num):
    if num == 1:
        return 1
    return num + sum_numbers(num -1)


print(sum_numbers(5))# ➞ 15

print(sum_numbers(1))# ➞ 1

print(sum_numbers(12))# ➞ 78

