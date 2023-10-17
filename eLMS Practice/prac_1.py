month = input("Month: ")
unit_used = float(input("Unit_used: "))
base_bill = 18

if (unit_used>=0 and unit_used<=50):
    total_bill = base_bill + (unit_used * 4.35)
elif (unit_used>=51 and unit_used<=100):
    total_bill = base_bill + (50-0) * 4.35 + (unit_used * 10.75)
