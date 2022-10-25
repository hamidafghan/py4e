number = input("What is your phone number, without zero: ")
code = int(number[:2])


match code:
    case 74:
        print("Salaam")
    case 77:
        print("MTN")
    case 78:
        print("Etisalat")
    case 79:
        print("Roshan")
