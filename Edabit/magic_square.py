from posixpath import split


def magic_square_game(alice, bob):
    alice2 = bob[0] - 1
    bob2 = alice[0] - 1
    alice_num = alice[1]
    alice_num = int(alice_num[alice2])
    bob_num = bob[1]
    bob_num = int(bob_num[bob2])
    if even_odd(alice[1]) == False and even_odd(bob[1]) == True:
        if alice_num == bob_num:
            return True
        else:
            return False
    else:
        return False
def even_odd(nummber):
    a = int(nummber[0]) + int(nummber[1]) + int(nummber[2])
    if a % 2 != 0:
        return False
    else:
        return True

# print(magic_square_game([2, "100"], [1, "101"]))
# # ➞ False


# print(magic_square_game([3, "111"], [2, "011"]))
# # ➞ True

# print(magic_square_game([1, "010"], [3, "101"]))
# # ➞ False

def test_magic_square():
    assert magic_square_game([1, "001"], [1, "101"]) == False
# ➞ True
