#Second Largest Element: Write a Python program to find the second largest element in a list.
#Input: [12, 45, 78, 34, 56]
#Output: 56
user_input = list(map(int, input().split(",")))
largest = user_input[0]
for i in user_input:
    if (largest < i):
        largest = i
print(f"The largest value is: {largest}")
second_largest = user_input[0]
for j in user_input:
    if (j == largest): continue
    if (second_largest < j):
        second_largest = j
print(f"The second largest number is: {second_largest}")



#Maximum Product of Two Integers: Write a Python program to find the maximum product of two integers in a list.
#Input: [2, 3, 5, 7, 11]
#Output: 77
numbers = list(map(int, input().split(",")))
max = numbers[0]
j = 1
pro = 1
for i in numbers:
    if i > max:
        max = i
        pro = max * j
        j = max
print(pro)


#Perfect Square Check: Write a function to check if a number is a perfect square.
#Input: 16
#Output: True
num = float(input())
i = 0
is_square = False
while i < num:
    if num == i**2:
        is_square = True
        break
    i += 1
print(is_square)

#Or,
d=int(input())
p=d**(1/2)
if float(p)==int(p):
    print("true")
else:
    print("false")


#Check if a string is a palindrome (reads the same forwards and backwards) without using built-in functions
n = input("Enter a word: ")
n = n.lower()
is_palindrome = True

i = 0
j = 1
while i < len(n)//2:
    if n[i] == n[i-j]:
        i += 1
        j += 2
    else:
        is_palindrome = False
        break

print(is_palindrome)

#Or,
word = input()
word = word.lower()

lst1 = [x for x in word]

lst2 = lst1[:]
lst2.reverse()

if lst1 == lst2:
    is_pelindrom = True
else:
    is_pelindrom = False

print(is_pelindrom)



# Shopno offer-
lst = ["chiken","coconut","fish","coca-cola","oats","oil","toast","lexux","biscuit","noodles"]
n=input("The name of the product: ")

if n in lst:
    n1=int(input("The price: "))
    print(f"Product name : {n}")
    print(f"Product price : {n1}")
    print("Date:12.10.23 ")
else:
    print(f"Product is not available.")
if n==lst[2]:
    print("You will get a gift")
