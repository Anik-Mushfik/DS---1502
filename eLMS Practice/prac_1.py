lst = [2,12,23,56,64,81,92]
search = int(input())
Found = False
for i in lst:
    if i == search:
        Found = True
        break
if Found:
    print("Found")
else:
    print("Not Found")


