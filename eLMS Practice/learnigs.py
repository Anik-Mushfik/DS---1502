def multiply(*numbers):
    total = 1
    for i in numbers:
        total *= i
    return total


print(multiply(1,2,3,4,5,6))



def save_user(**user):
    print(user)
    print(user["id"])
    for key, val in user.items():
        print(f"{key}: {val}")


save_user(id= 154, name= "anik", age= 21)


message = "a"
def greet(name):
    global message # Bad practice(try to avoid)
    message = "b"


greet(3)
print(message)


### Fizz Buzz algorithm
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    elif (input % 3 == 0):
        return "Fizz"
    elif (input % 5 == 0):
        return "Buzz"
    else:
        return input
    

print(fizz_buzz(3))

# Or,
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if (input % 3 == 0):
        return "Fizz"
    if (input % 5 == 0):
        return "Buzz"
    return input
    

print(fizz_buzz(17))


n=int(input())
def add():
    sum=0
    for i in range(1,n+1):
        a=int(input())
        b=int(input())
        c=a+b
        sum=sum+c 
    print(f"The addition is {sum}")

add()
