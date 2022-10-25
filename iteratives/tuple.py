# Tuple
# Ordered
# Unchangeable

students = ("Jamal", "Kamal", "Ali", "Parwin", "Kamal")

# print("Tuple: ", type(students))

# for student in students:
#     print(student)

# Adding new element *
# 1, need to cast to list 2.append 3.cast back to typle

# students = list(students)  # 1
# students.append("Mahtab")  # 2

# students = tuple(students)  # 3
# print(students)

# Access the element ( The same as list)

# check if the element is in typle
# if "Jamal" in students:
#     print("Yes, he is in.")

# unpack (Extract as variable)
# (jamal, *others, parwin) = students
# print(jamal, others, parwin)

# Join
# new_students = ("Sara", "Parwana")
# all_students = new_students + students

# print(all_students)

# To print the same tuple multiple times
# all_students = students * 10
# print(all_students)

# index (Search the value and return the index)
# try:
#     kamal = students.index("Parwina")
#     print(kamal)
# except:
#     print("The item is not in the tuple")

# count (cont how many kamal is in the tuple)
# times = students.count("Kamal")
# print(times)
