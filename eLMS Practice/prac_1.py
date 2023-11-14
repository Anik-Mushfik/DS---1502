lst = [2,12,23,56,64,81,92]
not_found = True
#linear search, Binary search
for i in lst:
    if i == 81:
        not_found = False
        break
if not_found:
    print("Not Found")
else:
    print("Found")