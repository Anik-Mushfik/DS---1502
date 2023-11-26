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


#calender
a = int(input())

if a == 1 :
    month = 'January'
elif a == 2 :
    month = 'February'
elif a == 3 :
    month = 'March'
elif a == 4 :
    month = 'April'
elif a == 5 :
    month = 'May'
elif a == 6 :
    month = 'June'
elif a == 7 :
    month = 'July'
elif a == 8 :
    month = 'August'
elif a == 9 :
    month = 'September'
elif a == 10 :
    month = 'October'
elif a == 11 :
    month = 'November'
elif a == 12 :
    month = 'December'
else:
    print(f"invalid input")

if month == 'January' or month=='March' or month=='May' or month=='July' or month=='August' or month=='October' or month=='December':
    days = 31
elif month == 'April' or month=='June' or month=='September' or month=='November':
    days = 30
else:
    days = 28
print(f"Month: {month}, Days: {days}")

#or,
num = int(input("Enter a number between 1 to 12: "))
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
if 1<= num and num <=12:
    month = months[num-1]
    d31 = [0,2,4,6,7,9,11]
    d30 = [3,5,8,10,12]
    if months.index(month) in d31: 
        days = 31
    elif months.index(month) in d30:
        days = 30
    else:
        days = 28
    print(f"The month corresponding to {num} is {month} and it has {days} days.")
else:
    print(f"Invalid input. Please enter a number between 0 to 12.")



#voting
age = int(input("Enter your age: "))
if age>= 18:
    print(f"You are eligible for voting.")
else:
    print(f"You are not eligible for voting.")


#Week day
num = int(input("Enter a number between 1 to 7: "))
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
if 1<= num and num <=7:
    day = days[num-1]
    print(f"The day corresponding to {num} is {day}.")
else:
    print(f"Invalid input. Please enter a number between 0 to 7.")


#Sakharyui sir ct
'''
In the computer labs of UIU, 35 students can sit together for classes. Write a program in python,
that will take the number of students admitted in the first trimester of data science program. As the
students are taking admissions one-by-one, the department has decided to fill up the open sections
full to their capacity and then open a new section. For example, if 90 students are admitted, 3
sections will be needed. First section will be full first, 35 students then second section will be full
with another 35 students and the last section will have only 20 students. Your program will print
will be needed for these newly admitted students and the size of the last section.
'''

num = int(input("Enter the number of admitted students: "))
if num % 35 ==0:
    print(f"For {num} newly admitted students {(num // 35)} sections will be needed and the size of the last section is 35 students.")
else:
    print(f"For {num} newly admitted students {(num // 35) + 1} sections will be needed and the size of the last section is {num % 35} students.")




#14/11/2023
lst = [5,-1,3,6,8]
sum = 0
for i in lst:
    sum += i
avarage = sum/len(lst)
print(avarage)

max = lst[0]
for i in lst:
    if i > max:
        max = i
print(max)

#linear search, Binary search

#linear search -
lst = [2,12,23,56,64,81,92]
search = int(input())
Found = False
for i in lst:
    if i == search:
        Found = True
        break
if Found:
    print("Found")
else:
    print("Not Found")


#Frequency calculator-

lst = [1,2,2,1,3,3,5,7,1,8,8,1,2,3]
count = 0
for i in range(0,10):
    for j in lst:
        if i == j:
            count += 1
    if count != 0:
        print(f"{i} has occurd for {count} times.")
    count = 0

#or,
mylist = [1,2,2,1,3,3,5,7,1,8,8,1,2,3]
count = [0]*10 #count = [0,0,0,0,0,0,0,0,0,0]

for element in mylist:
    count[element] = count[element] + 1

for x in range(10):
    print(f"{x} occured for {count[x]} times.")



                                                                                        
#### Lab - 26/11/2023

students_marks = {
    '0152330101' : 19, 
    '0152330119' : 15, 
    '0152330123' : 12, 
}

while 1==1:
#while (True):
    student_ID = input("Enter Student ID: ") #key age theki thakle value modify hobe
    if student_ID == 'Q':
        break
    marks = int(input("Enter mark: "))

    students_marks[student_ID] = marks

print(students_marks)



students_marks = {}
for i in range(5):
    student_ID = input("Enter Student ID: ")
    marks = int(input("Enter mark: "))

    students_marks[student_ID] = marks

sum = 0
for mark in students_marks.values():
    sum += mark
avarage = sum/len(students_marks.values())
print(f"Avarage: {avarage}")




students_marks = {
    '0152330101' : 19, 
    '0152330119' : 15, 
    '0152330123' : 12, 
}

search_ID = input("Enter Student ID: ")
exist = False

for i in students_marks.keys():
    if i == search_ID:
        exist = True
        break

if exist:
    print(f"Mark: {students_marks[i]}")
else:
    print(f"Apologies! The Student Doesn't Exist.")


# Or, 
for id, marks in students_marks.items():
    if id == search_ID:
        print(f"Mark: {marks}")
    else:
        print(f"Apologies! The Student Doesn't Exist.")

# Or, 
if search_ID in students_marks.keys():
    print(f"The mark for {search_ID}: {students_marks[search_ID]}")
else:
    print(f"Apologies! The Student Doesn't Exist.")



# Word frequancy counter:
data = "The quick brown fox jumps over the lazy dog"
words = data.split() # Split funtion auto ekta list banaye

words_num = {}

for word in words:
    if word in words_num.keys():
        words_num[word.lower()] += 1
    else:
        words_num[word.lower()] = 1

print(words_num)



# Shopping Cart Total Bill - 
shopping_cart = {}

while True:
    product = input("Enter Product name: ")
    if product == 'Q':
        break
    price = int(input("Enter price: "))
    shopping_cart[product] = price

total = 0
for i in shopping_cart.values():
    total += i

print(f"Your Prodect List:")
for pro, prices in shopping_cart.items():
    print(f"{pro} : {prices} taka")
print(f"\nTotal bill: {total}")


# Shopping Cart Total Bill with Discounted bill -
shopping_cart = {}

while True:
    product = input("Enter Product name: ")
    if product == 'Q':
        break
    price = int(input("Enter price: "))
    shopping_cart[product] = price

total = 0
discount = 0
for i in shopping_cart.values():
    total += i
    if i>300:
        i -= (i*.1)
    discount += i

print(f"\nYour Prodect List:")
for pro, prices in shopping_cart.items():
    print(f"{pro} : {prices} BDT")
    
print(f"\nTotal bill: {total} BDT")
print(f"Discounted bill: {discount} BDT\n")
