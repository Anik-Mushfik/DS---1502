# Problem - 1:
old = {'Math':81, 'Physics':83,'Chemistry':87}
new = {}
for x in sorted(old.values(), reverse=True):
    for i,j in old.items():
        if x == j:
            new[i] = j

print([*new.items()])

# Or,
old = {}
n = int(input("Enter the number of subjects: "))
print("\nEnter the subject and numbers:\n")
for i in range(n):
    k = list((input().split()))
    old[k[0].title()] = int(k[1])
new = {}

for x in sorted(old.values(), reverse=True):
    for i,j in old.items():
        if x == j:
            new[i] = j

print([*new.items()])

# Or, Chat GPT-
# Sample data
my_counter = {'Math': 81, 'Physics': 83, 'Chemistry': 87}

# Sort the dictionary items in descending order by values and convert to a list of tuples
sorted_list = sorted(my_counter.items(), key=lambda item: item[1], reverse=True)

# Print the sorted lis
print(sorted_list)


# Problem - 2:
lst = [{'item': 'item1', 'amount': 400},
       {'item': 'item2', 'amount': 300},
       {'item': 'item1', 'amount': 750}]
new = {}

for dicts in lst:
    # dvl => dictionary values list
    dvl = list(dicts.values())
    if dvl[0] in new:
        new[dvl[0]] += dvl[1]
    else:
        new[dvl[0]] = dvl[1]

print(new)