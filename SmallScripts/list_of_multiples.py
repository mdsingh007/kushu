    def List_of_Multiples(num, length):
        num_ = num
        List_of_Multiples_ = []
        for elem in range(1, length + 1):
            number = elem * num_
            List_of_Multiples_.append(number)
        return List_of_Multiples_

    def List_of_Multiples2(num, length):
        return list(range(num, num*(length+1), num))

print(List_of_Multiples(7, 5))
print(List_of_Multiples2(7, 5))
