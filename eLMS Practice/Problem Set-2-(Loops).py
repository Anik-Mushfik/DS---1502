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


#Problem-2:
num = int(input())
for i in range(num, 0, -1):
    print(i, end=" ")

#Or,
num = int(input())
lst = list(reversed(range(1,num+1)))
for i in lst:
    print(i, end=" ")

#Or,    
num = int(input())
lst = list(map(int, (range(1, num+1))))
lst_2 = sorted(lst, reverse=True)
print(lst_2)
for i in lst_2:
    print(i, end=" ")

#Or,




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
lst = [1,1]
num = int(input("Enter a number: "))
for i in range(num):
    new_num = lst[-1] + lst[-2]
    lst.append(new_num)
new_lst = lst[:num]
print(f"The Fibonacci series up to the length of N is")
print(*new_lst)

#or,
n=int(input())
a,b=1,1
if n == 1:
    print(a) 
else:
    print(a,end=" ") 
    print(b,end=" ")
    for i in range(n-2):
        a,b=b,a+b
        print(b,end=" ")

#Or,
lst = [1,1]
num = int(input("Enter a number: "))
while (len(lst) <= num):
    new_num = lst[-1] + lst[-2]
    lst.append(new_num)
new_lst = lst[:num]
print(f"The Fibonacci series up to the length of N is")
print(*new_lst)

#Or, Chat GPT- (1 dile vul ashe.)
## Get user input for the desired length of the Fibonacci series
N = int(input("Enter the length of the Fibonacci series: "))

## Initialize the first two Fibonacci numbers
fibonacci_series = [1, 1]

## Generate the Fibonacci series up to the specified length
while len(fibonacci_series) < N:
    next_number = fibonacci_series[-1] + fibonacci_series[-2]
    fibonacci_series.append(next_number)

## Print the generated Fibonacci series
print("Fibonacci Series:")
for number in fibonacci_series:
    print(number, end=" ")



#Problem - 10:
N = int(input())
for i in range(1,N+2):
    if i % 2 == 0:
         i *= (-1)
print(i)


#Problrm - 11: Ami korsi-
number = int(input("Enter a number: "))

reversed_number = []

while number > 0:
    last_digit = number % 10
    reversed_number.append(last_digit)
    number = number // 10

for i in reversed_number:
    print(i, end="")

#Faiyaz -
n = int(input())
i = 0
while n > 0:
    i = n % 10
    print(i, end="")
    n = n // 10

#Or, Habibur korse-
n = int(input())
reverse = ""
# zero na hole loop chalabo e jonno while loop
while(n > 0):
    remainder = n % 10
    reverse += str(remainder) + ""
    n = n // 10
print(reverse)

#Or,
n= input()
for x in reversed(n):
    print(x, end='') 

#Or,GPT-
# Get user input for a number
number = int(input("Enter a number: "))

# Initialize variables for the reversed number and the remainder
reversed_number = 0

# Use a while loop to reverse the number
while number > 0:
    # Get the last digit of the number
    last_digit = number % 10
    # Append the last digit to the reversed number
    reversed_number = reversed_number * 10 + last_digit
    # Remove the last digit from the original number
    number = number // 10

# Print the reversed number
print("Reversed number:", reversed_number)


#Prolem - 12:
numbers = list(map(int, input().split()))
for i in numbers:
    if i == max(numbers):
        print(i)

#Or,Jodi while diye korte bole-
numbers = list(map(int, input().split()))
max = numbers[0]
i= 0
while i<len(numbers):
    print(numbers[i])
    if numbers[i] > max:
        max = numbers[i]
    i += 1
print(max)


#Problem - 13:
num = list(map(int, input().split()))
if len(num) == 1:
    print("Cannot do this")
else:
    odd = 0
    even = 0
    for i in range(len(num)):
        if i % 2 == 0:
            even += num[i]
        else:
            odd += num[i]
    print(f"Sum of the even index: {even}")
    print(f"Sum of the odd index: {odd}")
#Or,Huddai pechaisi-
list = []
print(f"Enter your numbers: (Enter 'f' when you are done.)")
choices = 0
while choices != 'f':
    choice = input()
    list.append(choice)
    choices = choice
else:
    list.pop()
    print(list)
if len(list) == 1:
    print("Not gonna work")
else:
    odd = 0
    even = 0
    for x in list:
        indx = list.index(x)
        if indx%2 == 0 and indx>0:
            even += int(x)
        elif indx == 0:
            even+= int(x)
        else:
            odd += int(x)
    print(f"Sum of odd index:{odd}")
    print(f"Sum of even index:{even}")

#Or,ektu kom pechaisi-
a = []
n = int(input("ENTER NUMBER OF ELEMENTS : "))
for i in range (n):
    a.append(input("ENTER ELEMENT : "))
print(a)
odd = 0
even = 0
for x in a:
    if n != 1 :
        indx = a.index(x)
        if indx%2 == 0 and indx>0:
            even += int(x)
        elif indx == 0:
            even+= int(x)
        else:
            odd += int(x)
        print(odd)
        print(even)
    else:
        print("Not gonna work")


#Problem - 14:
num = list(map(int, input("Enter the jersey number: ").split()))
single = []
duplicate = []
for n in num:
    if n in single:
        if n not in duplicate:
            duplicate.append(n)
    else:
        single.append(n)
if len(duplicate) == 0:
    print(f"No duplicates")
else:
    print("Duplicate jersey numbers:", end=" ")
    for d in duplicate:
        print(d, end=" ")

#Or, shomosha hoche ulta print hoye and list akare print hoye-
num = list(map(int, input("Enter the jersey number: ").split()))
single = []
double = []
while ( 0 < len(num)):
    n = num.pop()
    if n in single:
        double.append(n)
    else:
        single.append(n)
if len(double) == 0:
    print(f"No duplicates")
else:
    print(f"Duplicate jersey numbers: {double}")

#Or,
num = list(map(int, input("Enter the jersey number: ").split()))
single = []
duplicate = []
no_double = True

for n in num:
    if n in single:
        if n not in duplicate:
            no_double = False
            if not no_double and len(duplicate) == 0:
                print("Duplicate jersey numbers:", end=" ")
            print(n, end=" ")
            duplicate.append(n)
    else:
        single.append(n)

if no_double:
    print(f"No duplicates")

#Or, Habiburer-
jerseys = input().split()
j_numbers = [int (x) for x in jerseys]
duplicate = []
not_dupli = []
for i in j_numbers:
    if i in not_dupli:
        if i not in duplicate:
            duplicate.append(i)
    else:
        not_dupli.append(i)
if duplicate:
    print("Duplicate jersey numbers: ", end="")
    for j in duplicate:
        print(j, end=" ")
    print()
else:
    print("No duplicate")



#Problem - 15:
hours = list(map(int, input("Hours Worked: ").split()))
wage = list(map(int, input("Hourly Wage: ").split()))
for i in range(len(hours)):
    if (hours[i] > 40):
        regular = 40 * wage[i]
        over = (hours[i] - 40) * ((wage[i]) * 1.5)
        total = regular + over
        print(f"Employee {i+1}: {int(total)} BDT")
    else:
        total = hours[i] * wage[i]
        print(f"Employee {i+1}: {total} BDT")



#Problem - 16:
time = list(map(int, input("Enter times of the players: ").split()))
first = 0
second = 0
third = 0

if first == 0:
    first = min(time)
    print(f"First Place: {time.index(first)}")
    time[time.index(first)] = max(time) + 1

if second == 0:
    second = min(time)
    print(f"Second Place: {time.index(second)}")
    time[time.index(second)] = max(time) + 1

if third == 0:
    third = min(time)
    print(f"Third Place: {time.index(third)}")

#Or,
time = input().split()
time = [int(x) for x in time]
for i in time:
    if i == (sorted(time))[0]:
        print(f"First palce: {time.index(i)}")
    elif i == (sorted(time))[1]:
        print(f"Seccond palce: {time.index(i)}")
    elif i == (sorted(time))[2]:
        print(f"Third palce: {time.index(i)}")


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




n = int(input())
for row in range(1,n+1):
    for collum in range(1,n+1):
        if row == collum:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

for i in range(1,n+1):
    for j in range(i):
        print('*', end=" ")
    print()

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()

for i in range(1,n+1):
    print(i * '*')