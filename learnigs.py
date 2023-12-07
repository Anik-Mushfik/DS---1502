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