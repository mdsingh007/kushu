# -  Poker Full House -------------------------------------------------------------------

def is_full_house(hand):
    if len(hand) != 5:
        return False

    else:
        a = hand[0]
        b = [x for x in hand if x != a]
        c = hand[:]
        c.remove(a)
        return c



print(is_full_house(["A", "A", "A", "K", "K"]))# ➞ True

print(is_full_house(["3", "J", "J", "3", "3"]))# ➞ True

print(is_full_house(["10", "J", "10", "10", "10"]))# ➞ False

print(is_full_house(["7", "J", "3", "4", "2"]))# ➞ False