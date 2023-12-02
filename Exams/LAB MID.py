###  LAB MIDterm Section - BC : 
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
