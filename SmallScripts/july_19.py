import datetime

# -  Friday the 13th -------------------------------------------------------------------

def has_friday_13(mth, yr):
    dt = datetime.datetime(yr, mth, 13)
    return dt.strftime("%A") == 'Friday'



print(has_friday_13(3, 2020))# ➞ True

print(has_friday_13(10, 2017))# ➞ True

print(has_friday_13(1, 1985))# ➞ False


# -  Friday the 13th -------------------------------------------------------------------

def consecutive_combo(lst1, lst2):
    lst3 = lst1
    lst4 = lst2
    for elem in lst4:
        lst3.append(elem)
    lst3.sort()
    count = lst3[0]
    for elem in lst3:
        if elem != count:
            return False
        else:
            count += 1
    return True


print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))# ➞ True

print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))# ➞ False

print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))# ➞ False

print(consecutive_combo([44, 46], [45]))# ➞ True

# -  Friday the 13th -------------------------------------------------------------------

def format_date(txt):
    txt2 = txt.split("/")
    txt3 = [txt2[-1], txt2[1], txt2[0]]
    return "".join(txt3)


print(format_date("11/12/2019"))# ➞ "20191211"

print(format_date("12/31/2019"))# ➞ "20193112"

print(format_date("01/15/2019"))# ➞ "20191501"