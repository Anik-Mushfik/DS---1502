"""
Abul,36,Dhaka,12500
Babul,42,Dhaka,13400
Kamal,26,Chittagong,16000
Jamal,28,Rajshahi,17000
Karim,40,Dhaka,11400
"""


def salary_incriment(salary):
    if (salary < 15000):
        return salary+(salary*0.2)
    else:
        return salary+(salary*0.15)

file = open("D:/Python Study/DS---1502/CW/Lab_file/employee.txt", "r")
person_info = file.read()
lst = person_info.split('\n')
for i in range(len(lst)):
    data = lst[i].split(',')
    data[3] = salary_incriment(int(data[3]))
    data[3] = str(data[3])
    lst[i] = data
file.close()
print(lst)

new_sen = []
for i in lst:
    sentence = ""
    for j in i:
        sentence += j + ","
    sentence.rstrip()
    print(sentence)
    new_sen.append(sentence + "\n")

print(new_sen)

file = open("D:/Python Study/DS---1502/CW/Lab_file/employee.txt", "w")
file.write("")
file.close()

file = open("D:/Python Study/DS---1502/CW/Lab_file/employee.txt", "a")
for i in new_sen:
    file.write(i)
file.close()