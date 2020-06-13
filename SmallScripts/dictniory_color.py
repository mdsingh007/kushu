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

max_avg = 0
max_avg_2 = ''
min_avg = 0
min_avg_2 = ''
diffrence = 0

def print_average(grade_list):
    a_average = 0
    for elem in grade_list:
        a_average += elem
    average = a_average / len(grade_list)
    return average


i = 0
for key in classes:
    val = classes[key]

    if i == 0:
        min_grade = key
        min_count = len(val)
        min_avg = len(val)
        min_avg_2 = key
        i += 1

    if len(val) > max_count:
        max_grade = key
        max_count = len(val)

    if print_average(val) > max_avg:
        max_avg_2 = key
        max_avg = print_average(val)

    if print_average(val) <  min_avg:
        min_avg_2 = key
        min_avg = print_average(val)

    if len(val) < min_count:
        min_grade = val
        min_count = len(val)
    print("average of", key, "is", print_average(val))

        
print("the most number of students are in", max_grade, max_count)
print("the min number of students are in", min_grade, min_count)
print("maximum average is", max_avg_2)
print("minimum average is", min_avg_2)
print(max_count - min_count)




        