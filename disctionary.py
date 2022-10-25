student = {
    "name": "Jamal",
    "last_name": "Kamal",
    "year": 1998
}

# # Loop over the dictionary (Keys)
# for key in student.keys():
#     print(key)

# # Loop over value
# for value in student.values():
#     print(value)

# Loop over items
# for key, value in student.items():
#     print(key, value)

# print("Name", student.get("name"))
# print("Last Name", student.get("last_name"))
# print("Year", student.get("year"))

# Get all value
# print("Values", student.values())

# Get all keys
# print("Key", student.keys())

# Add new element
# student["grade"] = "A+"

# Update the exitsing element or create it (update or create)
# student.update({"age": 24})
# print(student)

# remove on eleemnt
# student.pop("year")
# student.popitem() # it remove the element form the last

# to delete the dictionary
# del student

#  To delete only one element (key)
# del student["name"]

# to clear the dictionaly
# student.clear()

# copy the dictionary
# new_student = student.copy()
# new_student = dict(student)

# print(new_student)

students = {
    "01": {
        "name": "Jamal",
        "last_name": "Kamal",
        "grade": 1
    },
    "02": {
        "name": "Parwin",
        "last_name": "Ali",
        "grade": 1
    },
    "03": {
        "name": "Omid",
        "last_name": "Wali",
        "grade": 2
    }
}
