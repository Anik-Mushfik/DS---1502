#Problem-1:
num = int(input())
for i in range(1, num+1):
    print(i, end=" ")
#Or,
##Get user input for the number
n = int(input("Enter a number: "))

##Create a list of numbers from 1 to n (inclusive)
numbers = list(range(1, n + 1))

##The * operator is used to unpack the elements of the list and pass them as separate arguments to the print() function, which then prints them with spaces in between.
print(*numbers)


#3
n = int(input())
for x in range(1,n+1):
    if x%2 ==0:
        print(0,end=" ")
    else:
        print(1, end=" ")


#4
n = int(input())
sum = 0
for x in range(0,n):
    user_input = float(input())
    sum += user_input
average = sum/n
print(f"Average: {average}")
print(f"Average: {sum/n}")


#max value
n = int(input())
max = float(input())
for x in range(0,n-1):
    user_input = float(input())
    if max<user_input:
        max = user_input
print(f"Max Value: {max}")


#5-
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if (num1 < num2):
    x = num1; y = num2
else:
    y = num1; x = num2
if x != y:
    for i in range(x, y+1):
        print(i**2, end=" ")
print("END")


#6-
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
divisors_num2 = []
divisors_num1 = []
for x in range(1, num1+1):
    if (num1 % x == 0):
        divisors_num1.append(x)
for y in range(1, num2+1):
    if (num2 % y == 0):
        divisors_num2.append(y)
gcd = 0
for z in divisors_num1:
    if (z in divisors_num2) and (z > gcd):
        gcd = z
print(f"GCD: {gcd}")
lcm = 0
count = 1
while lcm !=0:
    if (count % num1 == 0.0) and (count % num2 == 0.0):
        lcm = count
        print(f"LCM: {count}")
        break
    count += 1


#7
N = int(input())
factorial = 1
for i in range(1,N+1):
    factorial *= i
print(f"The factorial of {N} is {factorial}")


#8
N = int(input())
if N == 1:
    print(("Not prime"))
else:
    for i in range(1,N+1):
        if i == 1 or i == N: continue
        if N % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

#or,
N = int(input())
for i in range(1,N+1):
    if N == 1:
        print(("Not prime"))
        break
    if i == 1 or i == N: continue
    if N % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")




#17-
n = int(input("Enter the size of number: "))

for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()


#18-
n = int(input("Enter the size of number: "))

for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()


#18- 
n = int(input("Enter the size of number: "))

for i in range(1,n+1):
    for j in range(i):
        print(i**2, end=" ")
    print()
