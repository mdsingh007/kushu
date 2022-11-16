def make_box(number):
    space_line = number - 2
    arrangment = ""
    if number == 1:
        return "#" 
    if number == 2:
        return "##\n##"
    if space_line < 0:
        space_line = 0
    arrangment += ("#" * number)
    for elem in range(space_line):
        arrangment += "\n"
        arrangment += "#"
        arrangment += space_line * " "
        arrangment += "#"

    arrangment += "\n"
    arrangment += ("#" * number)
    return arrangment


    


print(make_box(5))
# ➞ [
#   "#####",
#   "#   #",
#   "#   #",
#   "#   #",
#   "#####"
# ]
print()
print(make_box(3))
# ➞ [
#   "###",
#   "# #",
#   "###"
# ]
print()
print(make_box(2))
# ➞ [
#   "##",
#   "##"
# ]
print()
print(make_box(1))
# ➞ [
#   "#"
# ]