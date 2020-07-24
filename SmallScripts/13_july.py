# -  In the Centre? -------------------------------------------------------------------

def is_central(txt):
    centre = int(len(txt)/2)
    if len(txt) % 2 == 0:
        return False
    elif txt[centre] != " ":
            return True
    else:
        return False



print(is_central("  #  "))# ➞ True

print(is_central(" 2 "))# ➞ False

print(is_central("@"))# ➞ True