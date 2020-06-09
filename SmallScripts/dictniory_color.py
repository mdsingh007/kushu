# colors = {"yellow":2, "green":9, "blue":15, "red":14, "orange":11}

# for elem in colors:
#     var = colors[elem]
#     if var > 10:
#         print(elem, var)


classes = {
        "Grade 1":[10, 9, 3, 1, 0, 4], 
        "Grade 2":[10, 9, 3, 10, 0, 4], 
        "Grade 3":[10, 9, 3, 1, 0, 4, 4, 2, 6, 3, 2, 5, 10, 4, 1], 
        "Grade 4":[10, 9, 3, 1, 0,2,4,6,3,5,2, 4], 
        "Grade 5":[10, 9, 3, 1, 4, 6, 0, 4]
        }

# grade = ""
# grade_len = classes.keys
max_grade = ''
max_count = 0
# lowest_grade = classes.keys[0]
min_grade = ''
min_count = 0

diffrence = 0



i = 0
for key in classes:
    val = classes[key]

    if i == 0:
        min_grade = key
        min_count = len(val)
        i += 1

    if len(val) > max_count:
        max_grade = key
        max_count = len(val)

    if len(val) < min_count:
        min_grade = key
        min_count = len(val)
        
print("the most number of students are in", max_grade, max_count)
print("the min number of students are in", min_grade, min_count)


print(max_count - min_count)




        