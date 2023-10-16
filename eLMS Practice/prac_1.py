employee_name = input("Enter employee name: ")
wrok_hour = int(input("Enter the work hours: "))
service_time = int(input("Enter years of work: "))
tasks_done = int(input("Enter tasks done: "))
tasks_given = int(input("Enter tasks given: "))

if (wrok_hour > 20 and service_time >= 2):
    productivity = tasks_done / tasks_given
    if productivity >= 0.5 and productivity <= .69:
        print(f"{employee_name} is eligible for the Bronze bonus")
    elif productivity >= .70 and productivity <= .89:
        print(f"{employee_name} is eligible for the Siver bonus")
    elif productivity >= .90 and productivity <= 1.00:
        print(f"{employee_name} is eligible for the Gold bonus")
    else:
        print(f"{employee_name} is eligible for the normal bonus")
else:
    print(f"{employee_name} is not eligible for a bonus")