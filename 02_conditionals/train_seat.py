seat_type = input("Enter the seat type (sleeper,AC, general, luxury)").lower()

match seat_type:
    case "sleeper":
        print("NO AC")
    case "AC":
        print("AC type")
    case "general":
        print("general type no ac no sleeping")
    case "luxury":
        print("World class facility with meals")
    