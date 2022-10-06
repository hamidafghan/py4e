# The list of students
students = ["Ahmad", "Kamal", "Jamal", "Ali", "Farzana"]
numbers = [9, 6, 8, 4, 6, 3, 4]

event_numbers = []
odd_numbers = []

# for student in students:
#     print("Ms.", student) if student == "Farzana" else print("Mr.", student)

for number in numbers:
    if number % 2 == 0:
        event_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Event Numbers", event_numbers)
print("Odd numbers", odd_numbers)
