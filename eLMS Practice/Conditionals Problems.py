#Problem-1:
name = input()
age = input()
print(f"Hello! My name is {name} and I am {age} years old.")


#Problem-2:
num = int(input())
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


#Practice Set-3:
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


#Practice-4:
x = int(input())
y = int(input())
z = int(input())
print(f"First value = {x}, Last value = {z}")


#Practice-5:
x = int(input())
y = int(input())
z = int(input())
if x>0 and x<180:
    if y>0 and y<180:
        if z>0 and z<180:
            if (x+y+z == 180):
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")

#Practice-5:
x = int(input())
y = int(input())
z = int(input())
if x+y+z == 180 and x>0 and y>0 and z>0:
    print("Yes")
else:
    print("No")


#Problem-6
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if ((a*a)+(b*b)) == (c*c):
    print("Special Triangel")
else:
    print("Not Special")


#Problem-7:
print("Tempareture Converter")
print("1. Celsius to Farenheit.")
print("2. Farenheit to Celcius.")
temp = int(input("Enter the choice of conversion: "))

if temp == 1:
    cels = float(input("Enter the temperature in Celsius: "))
    conv_1 = float(cels*1.8) + float(32)
    print(f"The converted temperature is: {int(conv_1)} F")
elif temp == 2:
    farn = float(input("Enter the temperature in Fahrenheit: "))
    conv_2 = float(farn-32) * float(5/9)
    print(f"The converted temperature is: {int(conv_2)} C")
else:
    print("Input Error!")


#Problem-8:
name = input("Enter item name: ")
price = float(input("Enter item price: "))
quantity = int(input("Enter item quantity: "))
total_price = price * quantity
print(f"The total price of {name} purchased: {total_price} BDT")


#Problem-9:
print("Chose an option to calculate the area- \n 1.Circle \n 2.Square \n 3.Rectangle \n 4.Triangle")
choice = int(input("Enter choice of shape: "))
if choice == 1:
    radious = int(input("Enter the radius: "))
    area = 3.14 * (radious*radious)
    print(f"Area of the circle: {area}")
elif choice == 2:
    length = int(input("Enter the length: "))
    area = length * length
    print(f"Area of the square: {area}")
elif choice == 3:
    side_1 = int(input("Enter the length for one side: "))
    side_2 = int(input("Enter the length for another side: "))
    area = side_1 * side_2
    print(f"Area of the rectangle: {area}")
elif choice == 4:
    base =int(input("Enter the base: "))
    height = int(input("Enter the height: "))
    area = int(.5 * base * height)
    print(f"Area of the triangle: {area}")
else:
    print("Input error!")


#Problem-10:
marks = float(input("Enter your final marks: "))
if marks<=100 and marks>=90:
    print("Grade: A, Outstanding")
elif marks<=89 and marks>=86:
    print("Grade: A-, Excellent")
elif marks<=85 and marks>=82:
    print("Grade: B+, Very Good")
elif marks<=81 and marks>=78:
    print("Grade: B, Good")
elif marks<=77 and marks>=74:
    print("Grade: B-, Above Average")
elif marks<=73 and marks>=70:
    print("Grade: C+, Average")
elif marks<=69 and marks>=66:
    print("Grade: C, Below Average")
elif marks<=65 and marks>=62:
    print("Grade: C-, Poor")
elif marks<=61 and marks>=58:
    print("Grade: D+, Very Poor")
elif marks<=57 and marks>=55:
    print("Grade: D, Pass")
elif marks<55 and marks>=0:
    print("Grade: F, Fail")
else:
    print("Input Error!")


#Problem-11:
name = input("Enter employee name: ")
work_hour = int(input("Enter the work hours: "))
years_work = int(input("Enter years of work: "))
done_tasks = int(input("Enter tasks done: "))
tasks_given = int(input("Enter tasks given: "))
productivity = done_tasks / tasks_given
if work_hour>20 and years_work>=2:
    if productivity>=0.5 and productivity<=0.69:
        print(f"{name} is eligible for the Bronze bonus")
    elif productivity>=0.70 and productivity<=0.89:
        print(f"{name} is eligible for the Silver bonus")
    elif productivity>=0.90 and productivity<=1.00:
        print(f"{name} is eligible for the Gold bonus")
    else:
        print(f"{name} is eligible for the normal bonus")
else:
    print(f"{name} is not eligible for a bonus")



#Practice-12:
rich  = int(input("Number of rich people: "))
poor = int(input("Number of poor people: "))
if rich > poor :
    print("Do not steal.")
if rich < poor :
    if poor%4 == 0 and rich%3 ==0:
        print("Steal")
    else:
        print("Do not steal")


#Problem-13:
letter = input().lower()
if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
    print("Vowel")
else:
    print("Not a Vowel")


#Practice-14:
run = int(input("Runs: "))
over_bowled = int(input("Over bowled: "))
target = int(input("Target: "))
run_remain = target - run
over_remain = 20 - over_bowled
runrate = run / over_bowled
estimated_run = float(runrate) * float(over_remain)
if estimated_run > run_remain:
    print("Might win")
else:
    print("Might lose")


#Problem-15:
weight = int(input())
if weight%2==0 and weight>2:
    print('Yes')
else:
    print('No')
