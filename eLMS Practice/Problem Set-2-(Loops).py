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
print(*numbers, sep=",")


#Problem-3:
n = int(input())
for x in range(1,n+1):
    if x%2 ==0:
        print(0,end=" ")
    else:
        print(1, end=" ")


#Problem-4:
n = int(input())
sum = 0
for x in range(0,n):
    user_input = float(input())
    sum += user_input
average = sum/n
print(f"Average: {average}")
print(f"Average: {sum/n}")


#Max value:
n = int(input())
max = float(input())
for x in range(0,n-1):
    user_input = float(input())
    if max<user_input:
        max = user_input
print(f"Max Value: {max}")


#Problem-5:
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


#Problem-6:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
##GCD
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
##LCM
count = 1
while 1==1:
    if (count % num1 == 0.0) and (count % num2 == 0.0):
        #lcm = count
        print(f"LCM: {count}")
        break
    count += 1



#Problem-7:
N = int(input())
factorial = 1
for i in range(1,N+1):
    factorial *= i # factorial = factorial * i
print(f"The factorial of {N} is {factorial}")

#Or,
N = int(input("Enter the number: "))
i = 1
factorial = 1
while i < (N+1):
    factorial *= i
    i += 1
print(f"The factorial of {N} is {factorial}")


#Problem-8:
N = int(input())
if N == 1:
    print(("Not prime"))
else:
    for i in range(2,((N//2) + 1)):
        if N % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

#or, chole but valo hoye nai code ta-
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

# Saddam sirer solution:(vul silo thik korsi)
# code ta bujhte shohoj but boro. amar ta bujhte kom shohoj kintu choto ase.
N = int(input("Enter the number: "))
# ২ এর চেয়ে ছোট সব সংখ্যা এবং নেগেটিভ সংখ্যাও প্রাইম সংখ্যা নয়।
if N < 2:
    print("Not prime")
else:
    i = 2
    # ২ সবচেয়ে ছোট প্রাইম নম্বর।
    is_prime = True
    # কোনো সংখ্যাকে তার half এর চেয়ে বড় কোনো সংখ্যা দিয়ে ভাগ করলে ভাগশেষ(%) সবসময় শুণ্য থেকে বড় (>০) হয়।
    while i < (N/2):
        if N % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")



#Problem-9:



#17-
n = int(input("Enter the size of number: "))

for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()

#Or,
n=int(input())
for x in range(1,n+1):
	print(x*'*')


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
