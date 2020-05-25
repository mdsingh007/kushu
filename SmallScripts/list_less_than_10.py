a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 1, 3, 199, 3, 67, 39387, 2627]

answer = input("enter a number:")
answer = int(answer)
for element in a:
    if element < answer:
        print(element)
