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


#Problem-7:
print("Tempareture Converter")
print("1. Celsius to Farenheit.")
print("2. Farenheit to Celcius.")
temp = int(input("Enter the choice of conversion: "))

if temp == 1:
    cels = int(input("Enter the temperature in Celsius: "))
    conv_1 = float(cels*1.8) + float(32)
    print(f"The converted temperature is: {int(conv_1)} F")
elif temp == 2:
    farn = int(input("Enter the temperature in Fahrenheit: "))
    conv_2 = float(farn-32) * float(5/9)
    print(f"The converted temperature is: {int(conv_2)} C")
else:
    print("Input Error!")


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


