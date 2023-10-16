print("Tempareture Converter")
print("1. Celsius to Farenheit.")
print("2. Farenheit to Celcius.")
temp = int(input("Enter the choice of conversion: "))


if temp == 1:
    cels = int(input("Enter the temperature in Celsius: "))
    conv_1 = float(cels*1.8) + float(32)
    print(f"The converted temperature is: {int(conv_1)}F")
elif temp == 2:
    farn = int(input("Enter the temperature in Fahrenheit: "))
    conv_2 = float(farn-32) * float(5/9)
    print(f"The converted temperature is: {int(conv_2)}C")
else:
    print("Input Error!")