#grade calculator
num = float(input("Enter your marks: "))
if num < 55 and num >=0:
    print("Grade: F")
elif num >= 55 and num<58:
    print("Grade: D")
elif num >= 58 and num<62:
    print("Grade: D+")
elif num >= 62 and num<66:
    print("Grade: C-")
elif num >= 66 and num<70:
    print("Grade: C")
elif num >= 70 and num<74:
    print("Grade: C+")
elif num >= 74 and num<78:
    print("Grade: B-")
elif num >= 78 and num<82:
    print("Grade: B")
elif num >= 82 and num<86:
    print("Grade: B+")
elif num >= 86 and num<90:
    print("Grade: A-")
elif num >= 90 and num<=100:
    print("Grade: A")
else:
    print("Input Error!")