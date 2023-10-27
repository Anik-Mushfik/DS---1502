#Question 1:
"""
Write a program to take in the name and age as user inputs. Print a message in the terminal
and make Python introduce yourself.

Example:
Input=>
John Doe
53 
Output (in Terminal)=>
Hello! My name is John Doe and I am 53 years old.
"""

name = input()
age = input()
print("Hello! My name is " + name +" and I am " + age +" years old.")


#Question 2
"""
Write a program to take a number as user input and check if the number is odd or even. Print
the label: "The number is odd/even".

Example:
Input=>     Output (in Terminal)=>
2           The number is even
15          The number is odd
32          The number is even
"""

#if er sentence er por : dite hobea
#% diye vagshesh ber kora hoye
#else er por : dite hobe

number = float(input())
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
