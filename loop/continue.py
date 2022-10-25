numbers = [1,2,3,4,5,6,7,8,9,10]
numbers = [3,6,8,5,9,7,10,12,11,5,4,2,1]
students = ["Jamal", "Kamal", "Ali", "Parwin"]
event_count = 0
odd_count = 0



for number in numbers:

    # ignore/skip the number 5
    if number == 5:
        continue

    print(number)

for student in students:
    if(student == "Ali"):
        continue

    print(student)

for number in numbers:
    # skip the odd numbers
    if number % 2 != 0:
        continue

    event_count = event_count + 1

for number in numbers:
    # skip the even numbers
    if number % 2 == 0:
        continue

    odd_count = odd_count + 1

print(event_count, odd_count)