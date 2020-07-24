# -  Remove Repeated Letters -------------------------------------------------------------------

def unrepeated(txt):
    txt2 = []
    for elem in txt:
        if elem not in txt2:
            txt2.append(elem)
    return "".join(txt2)


print(unrepeated("hello"))# ➞ "helo"

print(unrepeated("aaaaa"))# ➞ "a"

print(unrepeated("WWE!!!"))# ➞ "WE!"    

print(unrepeated("call 911"))# ➞ "cal 91"

# -  Tallest Skyscraper -------------------------------------------------------------------

def tallest_skyscraper(lst):
    for index, elem in enumerate(lst):
        if 1 in elem:
            return len(lst) - index



print(tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]))# ➞ 3

print(tallest_skyscraper([
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]))# ➞ 4

print(tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
]))# ➞ 2


# -  Track the Robot (Part 1) -------------------------------------------------------------------

def track_robot(clist):
    r_l = 0
    u_d = 0

    for txt in clist:

        lst = txt.split()
        direction = lst[0]
        dist = lst[1]
        dist = int(dist)
        
        if direction == "right":
            r_l += dist
        if direction == "left":
            r_l -= dist
        if direction == "up":
            u_d += dist
        if direction == "down":
            u_d -= dist
    
    return [r_l, u_d]
    


print(track_robot(["right 10", "right 10"]))
# [10, 0]
print(track_robot(["right 10", "up 50", "left 30", "down 10"]))# ➞ [-20, 40]

# track_robot([]) ➞ [0, 0]
# // If there are no instructions, the robot doesn't move.

# track_robot(["right 100", "right 100", "up 500", "up 10000"]) ➞ [200, 10500]


# -  Track the Robot (Part 2) -------------------------------------------------------------------
print("Track the Robot (Part 2) -------------------------------------------------------------------")


def track_robot2(*dist):
    n_s = 0
    e_w = 0
    for count, elem in enumerate(dist):
        if count % 4 == 0:
            n_s += elem
        if count % 4 == 1:
            e_w += elem
        if count % 4 == 2:
            n_s -= elem
        if count % 4 == 3:
            e_w -= elem
        
    return [e_w, n_s]


    # n_s += n
    # e_w += e
    # n_s -= s
    # e_w -= w
    # return [e_w, n_s]




print(track_robot2(20, 30, 10, 40))# ➞ [-10, 10]

print(track_robot2())# ➞ [0, 0]

print(track_robot2(-10, 20, 10))

print(track_robot2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) #, [6, 5])

# try:

#     print(track_robot2(-10, 20, 10))# ➞ [20, -20]
#     # The amount to move can be negative.
# except TypeError:
#     print([0, 0])



# -  2nd largest number -------------------------------------------------------------------

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

b = 0

for elem in a:
    if elem > b:
        b = elem

a.remove(b)
c = 0
while True:
    for elem in a:
        if elem > c:
            c = elem
    if b == c:
        a.remove(b)
        c = 0
    else:
        break

print(c)

a = [8, 9, 10, 10, 10]

l = 0
sl = 0

for elem in a:
    if elem > l:
        sl = l
        l = elem

print(sl)