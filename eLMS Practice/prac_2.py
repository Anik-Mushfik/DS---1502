n1 = int(input())
n2 = int(input())

## GCD - 
gcd_n1 = [1,n1]
gcd_n2 = [1,n2]

for i in range(2,((n1//2)+1)):
    if n1%i == 0:
        gcd_n1.append(i)
for j in range(2,((n2//2)+1)):
    if n2%j == 0:
        gcd_n2.append(j)

for x in sorted(gcd_n1):
    if x in gcd_n2:
        pri = x
print(f"GCD: {pri}")

## LCM -
lcm_n1 = []
lcm_n2 = []

for i in range(1,n1+1):
    x = n1*i
    lcm_n1.append(x)
for j in range(1,n2+1):
    y = n2*j
    lcm_n2.append(y)

for a in sorted(lcm_n1):
    if a in lcm_n2:
        print(f"LCM: {a}")
        break
