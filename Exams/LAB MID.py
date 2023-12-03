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
print(f"\tMusfique's Chocolate Factory")
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

# Or, (jamee)
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