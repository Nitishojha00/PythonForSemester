s=int(input("enter day of week:"))

match s:
    case 1:
        print("Monday")
    case 2 :
        print("Tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case default:
        print("holiday")
