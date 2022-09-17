# Get the phone number from user -> Prompt
number = input("Please enter your phone number: Without zero 9 digit: ")

# Get the operator code
number = number[0:2]

# convert to integer
number = int(number)

# Get the operator name
# 70 AWCC, 74 Salaam, 76,77 MTN, 78 Etisalat, 79 Roshan

if number == 70:
    print("AWCC")
elif number == 74:
    print("Salaam")
elif number == 76 or number == 77:
    print("MTN")
elif number == 78:
    print("Etisalat")
elif number == 79:
    print("Roshan")
else:
    print("No valid number")
