class IceCream(object):
    def __init__(self, flavor, num_sprinkles):
        self.flavor = flavor
        self.num_sprinkles = num_sprinkles

    def sayName():
        return IceCream('Chocolate', 12)


ice1 = IceCream("Chocolate", 13)         # value of 23
ice2 = IceCream("Vanilla", 0)           # value of 5
ice3 = IceCream("Strawberry", 7)         # value of 17
ice4 = IceCream("Plain", 18)             # value of 18
ice5 = IceCream("ChocolateChip", 3)      # value of 8

def sweetest_icecream(lst):
    sweetest = 0
    a = []
    for elem in lst:
        if elem.flavor == "Chocolate":
            a.append(10 + elem.num_sprinkles)
        if elem.flavor == "Vanilla":
            a.append(5 + elem.num_sprinkles)
        if elem.flavor == "ChocolateChip":
            a.append(5 + elem.num_sprinkles)
        if elem.flavor == "Strawberry":
            a.append(10 + elem.num_sprinkles)
        if elem.flavor == "Plain":
            a.append(0 + elem.num_sprinkles)

    a.sort()
    sweetest = a[-1]
    return sweetest


# print(sweetest_icecream([ice1, ice2, ice3, ice4, ice5]))

# IceCream.sayName()

# ice1 = IceCream("Chocolate", 13)         # value of 23
# ice9 = IceCream.sayName()


class Employee(object):
    def __init__(self, fn, ln, s):
        self.firstname = fn
        self.lastname = ln
        self.salary = s



def from_string(dat):
    dat2 = dat.split("-")

    obj = Employee(dat2[0], dat2[1], dat2[2])
    return obj



emp1 = Employee("Mary", "Sue", 60000)
emp2 = from_string("John-Smith-55000")


print(emp1.firstname)# ➞ "Mary"

print(emp1.salary)# ➞ 60000

print(emp2.firstname)# ➞ "John"

print(emp2.salary)# ➞ 55000


def empty_values(lst):
    a = lst
    for index, elem in enumerate(lst):
        if type(elem) == int:
            a[index] = 0
        elif type(elem) == float:
            a[index] = 0.0
        elif type(elem) == str:
            a[index] = ""
        elif type(elem) == bool:
            a[index] = False
        elif type(elem) == list:
            a[index] = []
        elif type(elem) == tuple:
            a[index] = ()
        elif type(elem) == set:
            a[index] = set{}
        else:
            a[index] = None
    return a


print(empty_values([1, 2, 3]))# ➞ [0, 0, 0]

print(empty_values([7, 3.14, "cat", {1}]))# ➞ [0, 0.0, ""]

print(empty_values([[1, 2, 3], (1,2,3), {1,2,3}]))# ➞ [[], (), set()]

print(empty_values([[7, 3.14, "cat"]]))# ➞ [[]]

print(empty_values([None]))# ➞ [None]



