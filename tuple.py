# Tuple
# Ordered
# Unchangeable

students = ("Jamal", "Kamal", "Ali", "Parwin")

# print("Tuple: ", type(students))

# for student in students:
#     print(student)

# Adding new element *
# 1, need to cast to list 2.append 3.cast back to typle

students = list(students)  # 1
students.append("Mahtab")  # 2

students = tuple(students)  # 3
print(students)
