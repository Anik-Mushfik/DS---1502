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
    print(f"Invalid input. Please enter a number between 0 to 7.")
