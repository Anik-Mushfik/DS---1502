lst = [1,2,2,1,3,3,5,7,1,8,8,1,2,3]
count = 0
for i in range(0,10):
    for j in lst:
        if i == j:
            count += 1
    if count != 0:
        print(f"{i} has occurd for {count} times.")
    count = 0

#or,
mylist = [1,2,2,1,3,3,5,7,1,8,8,1,2,3]
count = [0]*10 #count = [0,0,0,0,0,0,0,0,0,0]

for element in mylist:
    count[element] = count[element] + 1

for x in range(10):
    print(f"{x} occured for {count[x]} times.")