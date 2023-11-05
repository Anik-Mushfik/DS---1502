# How to Reverse a Number with a While Loop
number = 67890
reversed_number = 0

while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
    
print(reversed_number)

# Returns: 9876