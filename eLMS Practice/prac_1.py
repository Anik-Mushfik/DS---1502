rich  = int(input("Number of rich people: "))
poor = int(input("Number of poor people: "))
if rich > poor :
    print("Do not steal.")
if rich < poor :
    if poor%4 == 0 and rich%3 ==0:
        print("Steal.")
    else:
        print("Do not steal")
