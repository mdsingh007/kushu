def percent_filled(lst):
    a = []
    b = []
    for elem in lst:
        for l in elem:
            if l == "o":
                a.append(l)
            if l == " ":
                b.append(l)

    c = len(a) * 100
    d = []

    for elem in lst:
        for l in elem:
            if l == "o" or l == " ":
                d.append(l)

    e = int(c / len(d))
    return str(e) + "%"


print(percent_filled([
  "#####",
  "#oo #",
  "#ooo#",
  "#####"
]))# ➞ "25%"