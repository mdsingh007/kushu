st_marks = {
    "Manish": 5,
    "Kushagra": 100,
    "Mridula": 95,
    "Kashvi": 1,
    "Dadu": 10,
    "Dadi": 20,
}
maximum_marks = 0
maximum_name = ""
minimum_marks = 100
minimum_name = ""
total_marks = 0
k = 0


# Learn to loop through dictionary, via keys and via both key/value enumeration.
# Print a list of all the student names in the class
# Print name and marks for all the students
# Print student and their mark in alphabetical order.
# Who has the maximum marks
# who has the minimum marks
# What is the difference between maximum and minimum marks
# Find sum of all the marks of all the students
# Find sum of all marks - secured by students whose name starts with k

all_keys = st_marks.keys()
# maximum_marks = st_marks["Manish"]
# maximum_name = "manish" 
for key in sorted(all_keys):

    print(key, st_marks[key])
    total_marks += st_marks[key]
    if st_marks[key] >  maximum_marks:
        maximum_marks = st_marks[key]
        maximum_name = key
    if st_marks[key] <  minimum_marks:
        minimum_marks = st_marks[key]
        minimum_name = key
    if key[0] == "K":
        k += st_marks[key]


print("maximum marks:", maximum_name, maximum_marks)
print("minimum marks:", minimum_name, minimum_marks)
print("diffrence:", maximum_marks - minimum_marks)
print(total_marks)
print(k)

print('----------------------------------------')
for name, mark in st_marks.items():
    print (name, mark)

print( sum(st_marks.values()) )
print( sum([x[1] for x in st_marks.items() if x[0].startswith('K')]) )