# Lists that are correlated

# students = [
#     'Jackie',
#     'Tito',
#     'Jermaine',
#     'Marlon',
#     'Michael'
# ]

# grades = [
#     95.2,
#     89.7,
#     82.0,
#     77.8,
#     96.5
# ]

# def get_grade(name):
#     global students
#     global grades
#     if name in students:
#         idx = students.index(name)
#         grade = grades[idx]
#     else:
#         grade = -1
#     return grade

# print(get_grade('Michael'))
# print(get_grade('Tito'))
# print(get_grade('Marlon'))

# def add_student(name, grade):
#     global students
#     global grades
#     students.append(name)
#     grades.append(grade)

# add_student('Janet', 100.0)

# for idx in range(len(students)):
#     name = students[idx]
#     grade = grades[idx]
#     print(f"{name:20}{grade:10.1f}")

# BUT, Dictionaries are BETTER

grades = {
    "Jackie": 96.5,
    "Tito": 91.5,
    "Jermaine": 88.7,
    "Merlon": 88.7,
    "Michael": 68.5
}

# CRUD
# Read
# LISTS:   val = grades[2]
# DICTIONARIES:
grade = grades['Jermaine']
print(grade)

# Create
# LISTS:    grades.append(100) / grades.insert(2,100)
# DICTIONARIES:
grades['Janet'] = 100.0
print(grades['Janet'])

# Update
# LISTS:    grades[5] = 105.0
# DICTIONARIES:
grades['Janet'] = 105.0
grades['Janet'] += 5
print(grades['Janet'])

# Delete
# LISTS:    del grades[5] / grades.pop(5)
# DICTIONARIES:
# grades.pop('Janet')
del grades['Janet']
# grades['Janet'] += 5
# grades['Janet'] = grades['Janet'] + 5
# print(grades['Janet'])

# for idx in range(len(grades)):
#     grade = grades[idx]
#     print(grade)

# Show all grades
for key in grades:
    grade = grades[key]
    print(f"{key:20}{grade:10.1f}")

# Curve all grades
for key in grades:
    # grade = grades[key]
    # grade += 5
    # grades[key] = grade
    grades[key] += 5

# Show all grades
for key in grades:
    grade = grades[key]
    print(f"{key:20}{grade:10.1f}")


# for name in grades:    # DEFAULT---GIVES EACH KEY
# for name in grades.keys():  # IDENTICAL TO DEFAULT
total = 0
for val in grades.values():  # JUST THE VALUES IF I DON'T NEED THE KEY
    total += val
avg = total / len(grades)
print(f"AVERAGE: {avg:.1f}")


for key, grade in grades.items():
    print(f"{key:20}{grade:10.1f}")







