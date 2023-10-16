#Lab-3
num = int(input())
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

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

#Practice Set - 1-3:
n1 = int(input())
n2 = int(input())
if n1 > n2:
    x = n1
    y = n2
else:
    x = n2
    y = n1
sum = x + y
print(f"Their sum is:{sum}")
dif = x - y
print(f"Their difference is:{dif}")
pro = x * y
print(f"Their product is:{pro}")
div = x / y
print(f"Their division is:{div}")

#Promo Code:
current_order = int(input())
month_order = int(input())

if(current_order > 500):
    if(month_order > 3000):
        print("10% PROMO CODE: BT46VG6")
    else:
        print("5% PROMO CODE: D467VF4")
else:
    print("NOT ELIGIBLE FOR PROMO!")

#Bonus Calc:
employee_name = input("Enter employee name: ")
wrok_hour = int(input("Enter the work hours: "))
service_time = int(input("Enter years of work: "))
tasks_done = int(input("Enter tasks done: "))
tasks_given = int(input("Enter tasks given: "))

if (wrok_hour > 20 and service_time >= 2):
    productivity = tasks_done / tasks_given
    if productivity >= 0.5 and productivity <= .69:
        print(f"{employee_name} is eligible for the Bronze bonus")
    elif productivity >= .70 and productivity <= .89:
        print(f"{employee_name} is eligible for the Siver bonus")
    elif productivity >= .90 and productivity <= 1.00:
        print(f"{employee_name} is eligible for the Gold bonus")
    else:
        print(f"{employee_name} is eligible for the normal bonus")
else:
    print(f"{employee_name} is not eligible for a bonus")