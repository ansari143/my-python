a = int(input("Enter your lucky number\n"))

match a:
    case 1:
        print("you won Charger")
    case 2:
        print("you won key")
    case 3:
        print("you won laptop")
    case _:
        print("Better next time")