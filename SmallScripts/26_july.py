# -  rolls -------------------------------------------------------------------

def rolls(lst):
    a = []
    multiplier = 1

    for elem in lst:
        a.append(elem*multiplier)

        if elem == 1:
            multiplier = 0

        elif elem == 6:
            multiplier = 2
        else:
            multiplier = 1

    return sum(a)




print(rolls([1, 2, 3]))# ➞ 4
# The second roll, 2, counts as 0 as a result of rolling 1.

print(rolls([2, 6, 2, 5]))# ➞ 17
# The 2 following the 6 was multiplied by 2.

print(rolls([6, 1, 1]))# ➞ 8
# The first roll makes the second roll worth 2, but the
# second roll was still 1 so the third roll doesn't count.


# -  The Conquering Queen -------------------------------------------------------------------

def can_capture(queens):
    match = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8}
    q_1 = queens[0]
    q_2 = queens[1]

    if q_1[0] == q_2[0] or q_1[1] == q_2[1]:
        return True
    elif match[q_1[0]] - int(q_1[1]) == match[q_2[0]] - int(q_2[1]) or match[q_1[0]] + int(q_1[1]) == match[q_2[0]] + int(q_2[1]):
        return True

    else:
        return False




print(can_capture(["A1", "H8"]))# ➞ True
# print(can_capture(["A1", "H8"]))# ➞ True
# # Your queen can move diagonally to capture opponents' piece.

# print(can_capture(["A1", "C2"]))# ➞ False
# # Your queen cannot reach C2 from A1 (although a knight could).

# print(can_capture(["G3", "E5"]))# ➞ True

def calculate_damage(your_type, opponent_type, attack, defense):
    damage = 0

    if your_type == "fire" and opponent_type == "grass":
        damage = 50 * (attack / defense) * 2
    elif your_type == "grass" and opponent_type == "fire":
        damage = 50 * (attack / defense) * 0.5
    if your_type == "fire" and opponent_type == "water":
        damage = 50 * (attack / defense) * 0.5
    elif your_type == "water" and opponent_type == "fire":
        damage = 50 * (attack / defense) * 2
    if your_type == "fire" and opponent_type == "electric":
        damage = 50 * (attack / defense) * 1
    elif your_type == "electric" and opponent_type == "fire":
        damage = 50 * (attack / defense) * 1
    if your_type == "water" and opponent_type == "grass":
        damage = 50 * (attack / defense) * 0.5
    elif your_type == "grass" and opponent_type == "water":
        damage = 50 * (attack / defense) * 2
    if your_type == "water" and opponent_type == "electric":
        damage = 50 * (attack / defense) * 0.5
    elif your_type == "electric" and opponent_type == "water":
        damage = 50 * (attack / defense) * 2
    if your_type == "grass" and opponent_type == "electric":
        damage = 50 * (attack / defense) * 1
    elif your_type == "electric" and opponent_type == "grass":
        damage = 50 * (attack / defense) * 1
    
    return damage
    

    



print(calculate_damage("fire", "water", 100, 100))# ➞ 25

print(calculate_damage("grass", "fire", 35, 5))# ➞ 175

print(calculate_damage("electric", "fire", 100, 100))# ➞ 50