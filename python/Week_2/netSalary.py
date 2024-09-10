# calculate net salary for employee

name = input("Please enter name : ")
hours = int(input("Please enter number of hours worked : "))
hourly_rate = float(input("Please enter hourly rate : "))

net = hours * hourly_rate
net = round(net, 2)

print(f"The net salary of {name} is ${net}")