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
