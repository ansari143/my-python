day = int(input("please enter the day of week\n"))

match day:
    case 1:
        print("It is sunday")
    case 2:
        print("It is Monday")
    case 3:
        print("It is Tuesday")
    case 4:
        print("It is Wednesday")
    case 5:
        print("It is Thrusday")
    case 6:
        print("It is Friday")
    case 7:
        print("It is Saturday")
    case _:
        print("It is Not week")