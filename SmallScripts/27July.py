
class student():
    def __init__(self, greeting):
        self.msg = greeting

    def sayName(self, greeting):
        return self.msg + ' Kushagra'

    @property
    def name(self):
        return 'Kushagra'


a = student("Hi")
print(a.sayName("asdfghjk"))
print( a.name )


class Calculater(object):
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2


class ones_threes_nines():
    def __init__(self, num):
        self.a = num

    @property
    def nines(self):
        return int(self.a/9)

    @property
    def ones(self):
        return int(self.a/1)

    @property
    def threes(self):
        return int(self.a/3)


n1 = ones_threes_nines(5)
n1.nines# ➞ 0
