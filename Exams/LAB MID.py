###  LAB MIDterm Section - BC : 

## Qustion - 1:
# Ascii code of 'A' is  65 and 'a' is 97. So there is 32 difference between them.

user_input = input("Enter a character: ")
asci = ord(user_input)

if (65<= asci <=90):
    asci += 32
    new = chr(asci)
    print(f"The lowercase is: {new}")
elif (98<= asci <= 122):
    asci -= 32
    new = chr(asci)
    print(f"The uppercase is: {new}")
else:
    print(f"Input Error!")


## Qustion - 2:
print(f"\tMUSFIQUE's Chocolate Factory")
print(f"\nWhich type of chocolate is it?")

typ = input("Eter M/m for Milk chocolate and W/w for White chocolate: ")
num = int(input("Enter number of chocolates in this batch: "))

if (typ.lower() == 'm'):
    if (20<= num <=24):
        pack = "Mini Pack"
        price = 120
    elif (25<= num <=29):
        pack = "Small Pack"
        price = 150
    elif (30<= num <=34):
        pack = "Regular Pack"
        price = 200
    elif (35<= num <=40):
        pack = "Mega Pack"
        price = 250
    else:
        pack = "Error in packing line"
        price = 0
        
    print(f"\n{pack}")
    print(f"Price is: {price}")

elif (typ.lower() == 'w'):
    if (35<= num <=40):
        pack = "Mega Pack"
        price = 250 + (250*.25)
    elif (30<= num <=34):
        pack = "Regular Pack"
        price = 200 + (200*.25)
    else:
        pack = "Error in packing line"
        price = 0

    print(f"\n{pack}")
    print(f"Price is: {float(price)}")

else:
    print("Input Error!")

# Or, (jamee korse)-
print("\t\t'Stark Industries Chocolate Factory'")
print()
print('What type of chocolate is it?')
user_input = input('Enter M/m for Milk chocolate and W/w for white chocolate: ').lower()
chocolate_num = int(input('Enter number of chocolate in this batch: '))

if user_input == 'm':
    if 20 <= chocolate_num <= 24:
        print(f"Mini Pack\nPrice is: {120}")
    elif 25 <= chocolate_num <= 29:
        print(f"Smaller Pack\nPrice is: {150}")
    elif 30 <= chocolate_num <= 34:
        print(f"Regular Pack\nPrice is: {200}")
    elif 35 <= chocolate_num <= 40:
        print(f"Mega Pack\nPrice is: {250}")
    else:
        print(f"Error in the production line\nPrice is: {0}")
else:
    if 30 <= chocolate_num <= 34:
        print(f"Regular Pack\nPrice is: {200 + (200 * 0.25)}")
    elif 35 <= chocolate_num <= 40:
        print(f"Mega Pack\nPrice is: {250 + (250 * 0.25)}") 
    else:
        print(f"Error in the production line\nPrice is: {0}")


## Qustion - 3:
num_stu = int(input("Enter num of students in class: "))
all_stu = []
all_mark = []

for i in range(1,(num_stu+1)):
    roll = int(input(f"Enter roll for student number {i}: "))
    all_stu.append(roll)

    mark = []
    eval1 = int(input("Enter marks in Evaluation number 1: "))
    mark.append(eval1)
    eval2 = int(input("Enter marks in Evaluation number 2: "))
    mark.append(eval2)
    eval3 = int(input("Enter marks in Evaluation number 3: "))
    mark.append(eval3)
    total = sum(mark) - min(mark)

    all_mark.append(total)

for j in range(num_stu):
    print(f"ID {all_stu[j]} got {all_mark[j]} in total")

high = max(all_mark)
h_index = all_mark.index(high)
h_stu = all_stu[h_index]

low = min(all_mark)
l_index = all_mark.index(low)
l_stu = all_stu[l_index]

print(f"{h_stu} got the highest mark ({high}) and {l_stu} got the lowest mark ({low})")
# Or,
num_stu = int(input("Enter num of students in class: "))
n = int(input("Enter num of evaluations: "))
all_stu = []
all_mark = []

for i in range(1,(num_stu+1)):
    roll = int(input(f"Enter roll for student number {i}: "))
    all_stu.append(roll)

    mark = []
    for j in range(1,n+1):
        eval = int(input(f"Enter marks in Evaluation number {j}: "))
        mark.append(eval)

    total = sum(mark) - min(mark)

    all_mark.append(total)

for j in range(num_stu):
    print(f"ID {all_stu[j]} got {all_mark[j]} in total")

high = max(all_mark)
h_index = all_mark.index(high)
h_stu = all_stu[h_index]

low = min(all_mark)
l_index = all_mark.index(low)
l_stu = all_stu[l_index]

print(f"{h_stu} got the highest mark ({high}) and {l_stu} got the lowest mark ({low})")
