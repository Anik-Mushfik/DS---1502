num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
##GCD
divisors_num2 = []
divisors_num1 = []
for x in range(1, num1+1):
    if (num1 % x == 0):
        divisors_num1.append(x)
for y in range(1, num2+1):
    if (num2 % y == 0):
        divisors_num2.append(y)
gcd = 0
for z in divisors_num1:
    if (z in divisors_num2) and (z > gcd):
        gcd = z
print(f"GCD: {gcd}")
##LCM
count = 1
while 1==1:
    if (count % num1 == 0.0) and (count % num2 == 0.0):
        #lcm = count
        print(f"LCM: {count}")
        break
    count += 1
