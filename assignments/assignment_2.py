# rate=10
# if user works more than 40 h so should pay 1.5 times extra

hour = float(input("hour: >>> "))
rate = float(input("rate: >>> "))

regular_horus = 40
extra_hours = hour - regular_horus
extra_rate = rate * 1.5

if hour > regular_horus:
    print(regular_horus * rate + extra_hours * extra_rate)
else:
    print(hour * rate)
